from django.test import TestCase
from factory import Sequence
from factory.django import DjangoModelFactory

from playground.proxy.models import VM, DCAsset


# Create your tests here.


class VMFactory(DjangoModelFactory):
    class Meta:
        model = VM
        django_get_or_create = ("hostname",)

    hostname = Sequence(lambda n: f"VM {n}")


class DCAssetFactory(DjangoModelFactory):
    class Meta:
        model = DCAsset
        django_get_or_create = ("hostname",)

    hostname = Sequence(lambda n: f"DCA {n}")


class TestModels(TestCase):
    def test_create_object(self):
        vm = VMFactory()
        dca = DCAssetFactory()
        assert "DCA" in dca.hostname
        assert "VM" in vm.hostname
