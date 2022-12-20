from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Hijos, Padres
from forms import Buscar, FamiliarForm
from django.views import View 

def index(request):
    return render(request, "ejemplo/saludar.html")

def monstrar_familiares(request):
  lista_bebes = lista_bebes.objects.all()
  lista_hijos = lista_hijos.objects.all()
  lista_padres = lista_padres.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_bebes": lista_bebes, "lista_hijos": lista_hijos, "lista_padres": lista_padres })

class BuscarBebes(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_bebé.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_bebes = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_bebes':lista_bebes})
        return render(request, self.template_name, {"form": form})

class BuscarHijos(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_hijos.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_hijos = Hijos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_hijos':lista_hijos})
        return render(request, self.template_name, {"form": form})

class BuscarPadres(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_padres.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_padres = Padres.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_padres':lista_padres})
        return render(request, self.template_name, {"form": form})


class ActualizarBebe(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar.familiar.html'
  initial = {"nombre":"", "apellido":"", "DNI":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      Familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=Familiar)
      return render(request, self.template_name, {'form':form,'bebe': Familiar})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito del registro del bebé {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'bebe': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarHijo(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar.hijos.html'
  initial = {"nombre":"", "apellido":"", "DNI":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      Hijos = get_object_or_404(Hijos, pk=pk)
      form = self.form_class(instance=Hijos)
      return render(request, self.template_name, {'form':form,'hijo': Hijos})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      Hijos = get_object_or_404(Hijos, pk=pk)
      form = self.form_class(request.POST ,instance=Hijos)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito del registro del hijo {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'hijo': Hijos,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class ActualizarPadre(View):
  form_class = FamiliarForm
  template_name = 'ejemplo/actualizar.padres.html'
  initial = {"nombre":"", "apellido":"", "DNI":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      Padres = get_object_or_404(Padres, pk=pk)
      form = self.form_class(instance=Hijos)
      return render(request, self.template_name, {'form':form,'padre': Padres})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      Padres = get_object_or_404(Padres, pk=pk)
      form = self.form_class(request.POST ,instance=Hijos)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito del registro del padre {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'padre': Padres,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "apellido":"", "dni":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})