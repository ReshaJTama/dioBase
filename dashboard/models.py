from django.db import models

# Create your models here.

class obatBase(models.Model):
	nameObat		= models.CharField(max_length=30,unique=True)
	qtyObat			= models.IntegerField()
	categoryObat	= models.CharField(max_length=50)
	tanggalObat		= models.DateTimeField(auto_now=True)
	kadaluarsaObat	= models.DateField()
	pic		= models.CharField(max_length=30)
	CategoryChoice = (
			('Pilih','Pilih Salah Satu'),
			('Batuk','Obat Batuk'),
			('Asma','Obat Asma'),
		)

	categoryObat2 = models.CharField(
						max_length = 10,
						choices=CategoryChoice,
						default='Pilih',
		)

	def __str__(self):
		return "{}.{}".format(self.id,self.nameObat)




class AppModels(models.Model):
		name = models.CharField(max_length=50)
		jumlah = obatBase.objects.count()
		choice_set = obatBase.objects.filter(nameObat__startswith="").only('nameObat')
		choiceMantap = [
			(
				(obatBase,obatBase)

			) for obatBase in choice_set.iterator()]

		Choices = models.CharField(max_length=9,choices=choiceMantap, default=1)
		def __str__(self):
			return "{}.{}".format(self.name)
		