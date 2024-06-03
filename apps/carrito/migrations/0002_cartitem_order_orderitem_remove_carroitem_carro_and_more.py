# Generated by Django 4.2.13 on 2024-05-23 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_activo'),
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='carrito.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='carroitem',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='carroitem',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='carro',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
        migrations.DeleteModel(
            name='CarroItem',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]