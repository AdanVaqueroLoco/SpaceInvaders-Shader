from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#ROJO

from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#AMARILLOOO
class Invasor_cuatro(Modelo):

    vivo=True
    contador_tiempo = 0.0
    tiempo_anterior = 0.0
    activos_enemigos = 1


    def __init__(self,shader, posicion_id, transformaciones_id, color_id):
        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05
        self.posicion = glm.vec3(0.55, 0.55,0.0)

        self.vertices = np.append(self.vertices,
            np.array(
                [0.0,0.0,0.0,1.0,  0.72, 0.30,0.30, 1.0], dtype="float32"
            ))
        for i in range(0,359,5):
            self.vertices = np.append(self.vertices,
                np.array(
                    [0.055 * math.cos(i * math.pi/180.0),0.055 * math.sin(i * math.pi/180),0.0,1.0,  0.72,0.30,0.30,1.0]
                , dtype="float32"))
        
        super().__init__(shader, posicion_id, transformaciones_id, color_id)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)
            

    def dibujar(self):
        if self.vivo:
            self.shader.usar_programa()
            gl.glBindVertexArray(self.VAO)

            gl.glUniformMatrix4fv(self.transformaciones_id,
                    1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


            gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

            gl.glBindVertexArray(0)
            self.shader.liberar_programa()
