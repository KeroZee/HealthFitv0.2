# Exercise class to create an object with attributes needed for the HTML
class Exercises():
    def __init__(self, desc, benefits, steps, image, videos):
        self.desc = desc
        self.benefits = benefits
        self.steps = steps
        self.image = image
        self.videos = videos

    def get_videos(self):
        return self.videos

    def get_image(self):
        return self.image

    def get_desc(self):
        return self.desc

    def get_benefits(self):
        return self.benefits

    def get_steps(self):
        return self.steps

    def set_videos(self, videos):
        self.videos = videos

    def set_image(self, image):
        self.image = image

    def set_desc(self, desc):
        self.desc = desc

    def set_benefits(self, benefits):
        self.benefits = benefits

    def set_steps(self, steps):
        self.steps = steps