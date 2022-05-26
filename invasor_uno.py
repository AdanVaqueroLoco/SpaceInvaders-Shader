from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

##VERDEE

class Invasor_uno(Modelo):

    vivo=True
    contador_tiempo = 0.0
    tiempo_anterior = 0.0
    activos_enemigos = 1

    def __init__(self, x, y, direccion, velocidad):
        self.extremo_izquierdo=0.05
        self.extremo_derecho=0.05
        self.extremo_inferior=0.05
        self.extremo_superior=0.05

        self.vertices = np.array(
            [
                -0.05, 0.05, 0.0, 1.0,  0.3,0.72,0.37,1.0, 
                0.05, 0.05, 0.0, 1.0,   0.3,0.72,0.37,1.0,  
                0.05, -0.05, 0.0, 1.0,   0.3,0.72,0.37,1.0, 
                -0.05, -0.05, 0.0, 1.0,   0.3,0.72,0.37,1.0, 
            ], dtype="float32"
        )

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
