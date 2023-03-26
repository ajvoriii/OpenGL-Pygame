import glm

class Light:
    def __init__(self, position=(3,3,-3), colour=(1,1,1)):
        self.position = glm.vec3(position)
        self.colour = glm.vec3(colour)
        # intensities
        self.Ia = 0.1 * self.colour  # ambient
        self.Id = 0.8 * self.colour  # diffuse
        self.Is = 1.0 * self.colour # specular
