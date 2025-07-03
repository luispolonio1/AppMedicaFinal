# En tu views.py de doctor

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from applications.doctor.models import CitaMedica, Atencion
from applications.core.models import Diagnostico
# views.py - Agregar esta vista para obtener horarios dinámicamente
from applications.doctor.forms.detalleAtencion import DetalleAtencionForm
from django.http import JsonResponse
from django.views.generic import View
from datetime import datetime, timedelta
from applications.core.models import Doctor
from applications.doctor.models import HorarioAtencion, CitaMedica

class ObtenerHorariosDisponiblesView(View):
    """
    Vista AJAX que devuelve los horarios disponibles de un doctor en una fecha específica
    """
    
    def get(self, request, *args, **kwargs):
        doctor_id = request.GET.get('doctor_id')
        fecha_str = request.GET.get('fecha')
        
        if not doctor_id or not fecha_str:
            return JsonResponse({'error': 'Faltan parámetros'}, status=400)
        
        try:
            doctor = Doctor.objects.get(id=doctor_id, activo=True)
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            
            # Obtener día de la semana (Monday=0, Sunday=6)
            dia_semana_num = fecha.weekday()
            
            # Mapear a los días como los tienes en tu modelo
            dias_semana = {
                0: 'lunes',
                1: 'martes', 
                2: 'miercoles',
                3: 'jueves',
                4: 'viernes',
                5: 'sabado',
                6: 'domingo'
            }
            
            dia_semana = dias_semana.get(dia_semana_num)
            
            # Obtener horarios del doctor para ese día
            horarios = HorarioAtencion.objects.filter(
                doctor=doctor,  # Asumiendo que hay relación con Doctor
                dia_semana=dia_semana,
                activo=True
            )
            
            if not horarios.exists():
                return JsonResponse({
                    'horarios': [],
                    'mensaje': f'El doctor no atiende los {dia_semana}s'
                })
            
            # Generar slots de tiempo disponibles
            slots_disponibles = []
            
            for horario in horarios:
                slots_disponibles.extend(
                    self._generar_slots_horario(
                        doctor, horario, fecha
                    )
                )
            
            return JsonResponse({
                'horarios': slots_disponibles,
                'mensaje': f'Horarios disponibles para {fecha_str}'
            })
            
        except Doctor.DoesNotExist:
            return JsonResponse({'error': 'Doctor no encontrado'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'Fecha inválida'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def _generar_slots_horario(self, doctor, horario, fecha):
        """
        Genera los slots de tiempo disponibles para un horario específico
        """
        slots = []
        duracion_cita = doctor.duracion_atencion  # minutos
        
        # Convertir horas a datetime para facilitar cálculos
        inicio = datetime.combine(fecha, horario.hora_inicio)
        fin = datetime.combine(fecha, horario.hora_fin)
        
        # Manejar intervalo de pausa
        pausa_inicio = None
        pausa_fin = None
        if horario.intervalo_desde and horario.intervalo_hasta:
            pausa_inicio = datetime.combine(fecha, horario.intervalo_desde)
            pausa_fin = datetime.combine(fecha, horario.intervalo_hasta)
        
        # Generar slots
        slot_actual = inicio
        while slot_actual + timedelta(minutes=duracion_cita) <= fin:
            
            # Verificar si el slot está en horario de pausa
            if pausa_inicio and pausa_fin:
                if slot_actual >= pausa_inicio and slot_actual < pausa_fin:
                    slot_actual += timedelta(minutes=duracion_cita)
                    continue
            
            # Verificar si ya hay cita agendada en este horario
            cita_existente = CitaMedica.objects.filter(
                doctor=doctor,
                fecha=fecha,
                hora_cita=slot_actual.time(),
                estado__in=['disponible', 'confirmada']  # Estados que bloquean el horario
            ).exists()
            
            if not cita_existente:
                slots.append({
                    'hora': slot_actual.strftime('%H:%M'),
                    'hora_display': slot_actual.strftime('%I:%M %p'),
                    'disponible': True
                })
            
            slot_actual += timedelta(minutes=duracion_cita)
        
        return slots

class AtenderPacienteView(PermissionRequiredMixin, TemplateView):
    template_name = 'doctor/citas/atencionCita.html'
    permission_required = 'doctor.add_atencion'

    def dispatch(self, request, *args, **kwargs):
        self.cita = get_object_or_404(CitaMedica, pk=self.kwargs['pk'])
        if self.cita.estado != 'disponible':
            messages.error(
                self.request,
                'Solo se pueden atender citas en estado Disponible.'
            )
            return redirect('doctor:cita_detail', pk=self.cita.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cita'] = self.cita
        context['diagnosticos'] = Diagnostico.objects.all().order_by('descripcion')
        context['title'] = f'Atender a {self.cita.paciente.nombre_completo}'
        return context

    def post(self, request, *args, **kwargs):
        try:
            atencion = Atencion.objects.create(
                paciente=self.cita.paciente,
                presion_arterial=request.POST.get('presion_arterial') or None,
                pulso=int(request.POST.get('pulso')) if request.POST.get('pulso') else None,
                temperatura=float(request.POST.get('temperatura')) if request.POST.get('temperatura') else None,
                frecuencia_respiratoria=int(request.POST.get('frecuencia_respiratoria')) if request.POST.get('frecuencia_respiratoria') else None,
                saturacion_oxigeno=float(request.POST.get('saturacion_oxigeno')) if request.POST.get('saturacion_oxigeno') else None,
                peso=float(request.POST.get('peso')) if request.POST.get('peso') else None,
                altura=float(request.POST.get('altura')) if request.POST.get('altura') else None,
                motivo_consulta=request.POST.get('motivo_consulta'),
                sintomas=request.POST.get('sintomas'),
                tratamiento=request.POST.get('tratamiento'),
                examen_fisico=request.POST.get('examen_fisico') or None,
                examenes_enviados=request.POST.get('examenes_enviados') or None,
                comentario_adicional=request.POST.get('comentario_adicional') or None,
                es_control=bool(request.POST.get('es_control'))
            )

            diagnosticos_ids = request.POST.getlist('diagnostico')
            if diagnosticos_ids:
                atencion.diagnostico.set(diagnosticos_ids)

            self.cita.estado = 'Atendido'
            self.cita.save()

            messages.success(
                request,
                f'Atención médica registrada exitosamente para {self.cita.paciente.nombre_completo}.'
            )
            return redirect('doctor:atencion_detail', pk=atencion.pk)

        except ValueError as e:
            messages.error(request, f'Error en los datos ingresados: {str(e)}')
            return render(request, self.template_name, self.get_context_data())
        except Exception as e:
            messages.error(request, f'Error al registrar la atención: {str(e)}')
            return render(request, self.template_name, self.get_context_data())
