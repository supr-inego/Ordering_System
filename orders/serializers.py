from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name", "email"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "current_price"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "unit_price"]
        read_only_fields = ["unit_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "customer", "created_at", "items"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        for item in items_data:
            product = item["product"]
            qty = item["quantity"]

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                unit_price=product.current_price,  # snapshot
            )

        return order

    # BONUS: Update (simple student approach: delete items then re-add)
    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)

        instance.customer = validated_data.get("customer", instance.customer)
        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            for item in items_data:
                product = item["product"]
                qty = item["quantity"]
                OrderItem.objects.create(
                    order=instance,
                    product=product,
                    quantity=qty,
                    unit_price=product.current_price,
                )

        return instance
