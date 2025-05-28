from django.conf import settings

from vacation.models import Villa, Yacht, Vehicle


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product, count_product=1, update_count=False):
        model_type = product.__class__.__name__.lower()  # villa, yacht, vehicle
        prod_pk = f"{model_type}:{product.pk}"

        if prod_pk not in self.cart:
            self.cart[prod_pk] = {
                'count_prod': 0,
                'price_prod': str(product.price_per_day)
            }

        if update_count:
            self.cart[prod_pk]['count_prod'] = count_product
        else:
            self.cart[prod_pk]['count_prod'] += count_product

        self.save()

    def remove(self, product, model_type=None):
        if not model_type:
            model_type = product.__class__.__name__.lower()

        prod_pk = f"{model_type}:{product.pk}"

        if prod_pk in self.cart:
            del self.cart[prod_pk]
            self.save()

    def get_total_price(self):
        return sum(float(item['price_prod']) * int(item['count_prod']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __len__(self):
        return sum(int(item['count_prod']) for item in self.cart.values())

    def __iter__(self):
        cart = self.cart.copy()
        product_map = {
            'villa': Villa,
            'yacht': Yacht,
            'vehicle': Vehicle,
        }

        grouped_ids = {}
        for key in cart.keys():
            try:
                model_type, obj_id = key.split(":")
            except ValueError:
                continue
            grouped_ids.setdefault(model_type, []).append(obj_id)

        loaded_objects = {}
        for model_type, ids in grouped_ids.items():
            model_class = product_map.get(model_type)
            if model_class:
                loaded_objects[model_type] = {
                    str(obj.pk): obj for obj in model_class.objects.filter(pk__in=ids)
                }

        for key, item in cart.items():
            try:
                model_type, obj_id = key.split(":")
            except ValueError:
                continue

            obj = loaded_objects.get(model_type, {}).get(obj_id)
            if not obj:
                continue

            item['model_type'] = model_type
            item['product_id'] = obj_id
            item['the_object'] = obj
            item['total_price'] = float(item['price_prod']) * int(item['count_prod'])
            yield item
