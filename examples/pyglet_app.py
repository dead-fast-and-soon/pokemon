
import game.graphics.shaders
import pyglet
from konkyo.graphics import BatchRenderer
from konkyo.utils.gl import *
import glm

window = pyglet.window.Window(width=800, height=600)
program = game.graphics.shaders.program

# vert_shader = pyglet.graphics.shader.Shader(game.graphics.shaders.vertex_src, "vertex")
# frag_shader = pyglet.graphics.shader.Shader(game.graphics.shaders.fragment_src, "fragment")

# program = pyglet.graphics.shader.ShaderProgram(vert_shader, frag_shader)
# image = pyglet.image.load('assets/kris.png')

# tex_id = GLuint()
# glGenTextures(1, ctypes.byref(tex_id))

# pixels = (GLfloat * (3 * 4))(0.0, 0.0, 1.0,
#                              1.0, 0.0, 0.0,
#                              0.0, 1.0, 0.0,
#                              1.0, 1.0, 0.0)

# glBindTexture(GL_TEXTURE_2D, tex_id.value)
# glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 2, 2, 0, GL_RGB, GL_FLOAT, pixels)

model = glm.mat4(1.0)

view = glm.translate(glm.mat4(1.0), glm.vec3(400.0, 0.0, 0.0))

projection = glm.ortho(0, 800, 0, 600)

class Group(pyglet.graphics.Group):
    def __init__(self, program):
        super().__init__(program)

    def set_state(self):
        super().set_state()

        # glBindTexture(GL_TEXTURE_2D, image.get_texture().id)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # view_loc = gl_get_uniform_location(self.program._id, 'view')
        # proj_loc = gl_get_uniform_location(self.program._id, 'projection')
        gl_set_uniform_mat4(self.program._id, 'view', view)
        gl_set_uniform_mat4(self.program._id, 'projection', projection)

        # gl_set_uniform_mat4(view_loc, view)
        # gl_set_uniform_mat4(proj_loc, projection)
        # self.program['view'] = pyglet.matrix.Mat4()

    def unset_state(self):
        super().unset_state()
        # glDisable(GL_BLEND)

batch = BatchRenderer()
# batch = pyglet.graphics.Batch()

batch.add_indexed(4, GL_TRIANGLES, [0, 1, 2, 0, 2, 3],
          ("vertices2f", (0, 0, 0, 50, 50, 50, 50, 0)),
          ("colors3f", (1.0, 1.0, 1.0) * 4))
        #   ("tex_coords2f", (0, 0, 0, 1, 1, 1, 1, 0)))


while True:

    window.switch_to()
    window.dispatch_events()
    window.clear()

    batch.render()

    window.flip()
