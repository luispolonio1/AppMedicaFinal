# En tu views.py de doctor

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from applications.doctor.models import CitaMedica, Atencion
from applications.core.models import Diagnostico


class AtenderPacienteView(PermissionRequiredMixin, TemplateView):
    template_name = 'doctor/citas/atencionCita.html'
    permission_required = 'doctor.add_atencion'

    def dispatch(self, request, *args, **kwargs):
        cita = get_object_or_404(CitaMedica, pk=self.kwargs['pk'])
        if cita.estado != 'disponible':
            messages.error(
                self.request,
                'Solo se pueden atender citas en estado Disponible.'
            )
            return redirect('doctor:cita_detail', pk=cita.pk)
        self.cita = cita  # guardar la cita para usarla en get_context_data
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cita'] = self.cita
        context['diagnosticos'] = Diagnostico.objects.all().order_by('descripcion')
        context['title'] = f'Atender a {self.cita.paciente.nombre_completo}'
        return context

    def post(self, request, *args, **kwargs):
        cita = get_object_or_404(CitaMedica, pk=self.kwargs['pk'])

        try:
            # Crear la atención
            atencion = Atencion.objects.create(
                paciente=cita.paciente,
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

            # Agregar diagnósticos si fueron seleccionados
            diagnosticos_ids = request.POST.getlist('diagnostico')
            if diagnosticos_ids:
                atencion.diagnostico.set(diagnosticos_ids)

            # Cambiar estado de la cita a Atendido
            cita.estado = 'Atendido'
            cita.save()

            messages.success(
                request,
                f'Atención médica registrada exitosamente para {cita.paciente.nombre_completo}.'
            )
            return redirect('doctor:atencion_detail', pk=atencion.pk)

        except ValueError as e:
            messages.error(request, f'Error en los datos ingresados: {str(e)}')
            return render(request, self.template_name, self.get_context_data())

        except Exception as e:
            messages.error(request, f'Error al registrar la atención: {str(e)}')
            return render(request, self.template_name, self.get_context_data())


class AtencionDetailView(PermissionRequiredMixin, DetailView):
    model = Atencion
    template_name = 'doctor/atencion/detail.html'
    permission_required = 'doctor.view_atencion'
    context_object_name = 'atencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Atención Médica'
        context['cita'] = self.object.paciente.citamedica_set.filter(estado='Atendido').first()
        if not context['cita']:
            messages.warning(
                self.request,
                'No se encontró una cita médica asociada a esta atención.'
            )
        return context
