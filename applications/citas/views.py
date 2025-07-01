from django.shortcuts import render
from .forms import CitaMedicaForm
from applications.doctor.models import HorarioAtencion
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from applications.core.models import Paciente

def calendario(request):
    form = CitaMedicaForm()
    
    dias_disponibles = list(
        HorarioAtencion.objects.filter(activo=True).values_list('dia_semana', flat=True)
    )
    
    dia_indices = {
        'lunes': 1, 'martes': 2, 'miércoles': 3,
        'jueves': 4, 'viernes': 5, 'sábado': 6, 'domingo': 0
    }
    dias_permitidos = [dia_indices[d] for d in dias_disponibles if d in dia_indices]

    return render(request, 'citas/calendario.html', {
        'form': form,
        'dias_permitidos': dias_permitidos,
    })

@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            # Captura la fecha del input hidden
            fecha = request.POST.get('fecha')
            if not fecha:
                messages.error(request, "Error: No se seleccionó la fecha.")
                return redirect('citas:calendario')
            cita.fecha = fecha
            # Obtener el paciente asociado al usuario usando el id
            try:
                paciente = Paciente.objects.get(id=request.user.id)  # Aquí se obtiene el paciente por id
                cita.paciente = paciente
            except Paciente.DoesNotExist:
                messages.error(request, "Este usuario no está asociado a ningún paciente.")
                return redirect('citas:calendario')
            cita.save()
            messages.success(request, "¡Cita guardada exitosamente!")
            return redirect('citas:calendario')
    return redirect('citas:calendario')