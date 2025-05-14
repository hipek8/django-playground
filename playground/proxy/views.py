from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import VM


api = NinjaAPI()


class VMIn(Schema):
    name: str
    hostname: str


class VMOut(VMIn):
    id: int


@api.post("/vms")
def create_vm(request, payload: VMIn):
    vm = VM.objects.create(**payload.dict())
    return {"id": vm.id}


@api.get("/vms/{vm_id}", response=VMOut)
def get_vm(request, vm_id: int):
    vm = get_object_or_404(VM, id=vm_id)
    return vm


@api.get("/vms", response=list[VMOut])
def list_vms(request):
    qs = VM.objects.all()
    return qs


@api.put("/vms/{vm_id}")
def update_vm(request, vm_id: int, payload: VMIn):
    vm = get_object_or_404(VM, id=vm_id)
    for attr, value in payload.dict().items():
        setattr(VM, attr, value)
    vm.save()
    return {"success": True}


@api.delete("/vms/{vm_id}")
def delete_vm(request, vm_id: int):
    vm = get_object_or_404(VM, id=vm_id)
    vm.delete()
    return {"success": True}
