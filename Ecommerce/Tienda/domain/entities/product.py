class Product(object):

    def __init__(self, idProduct, title, description, price, category, image, slug):
        self.set_idProduct(idProduct)
        self.set_title(title)
        self.set_description(description)
        self.set_price(price)
        self.set_category(category)
        self.set_image(image)
        self.set_slug(slug)

    def set_idProduct(self, idProduct):
        self.idProduct = idProduct

    def set_title(self, title):
    	self.title = title

    def set_description(self, description):
    	self.description = description

    def set_price(self, price):
    	self.price = price

    def set_category(self, category):
    	self.category = category

    def set_image(self, image):
    	self.image = image

    def set_slug(self, slug):
    	self.slug = slug


    def get_idProduct(self):
        return self.idProduct

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_image(self):
        return self.image

    def get_category(self):
        return self.category

    def get_slug(self):
        return self.slug



    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

