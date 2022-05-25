from OpenGL.GL import *
from glew_wish import *
from Nave import *
from Modelo import *
import glfw
import math

#NARANJA


class Invasor_tres(Modelo):

    vivo=True
    contador_tiempo = 0.0
    tiempo_anterior = 0.0
    activos_enemigos = 1


    def __init__(self, x, y, direccion, velocidad):
        self.extremo_izquierdo=0.05
        self.extremo_derecho=0.05
        self.extremo_inferior=0.05
        self.extremo_superior=0.05
        self.posicion = glm.vec3(0.55, 0.55,0.0)

        self.vertices = np.array(
            [
                -0.05, 0.0, 0.0, 1.0,  0.72,0.53,0.3,1.0, 
                0.0, 0.05, 0.0, 1.0,   0.72,0.53,0.3,1.0,   
                0.05, 0.0, 0.0, 1.0,   0.72,0.53,0.3,1.0, 
                0.0, -0.5, 0.0, 1.0,   0.72,0.53,0.3,1.0, 
            ], dtype="float32"
        )


        super().__init__(shader, posicion_id, transformaciones_id, color_id)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)


    #def actualizar(self, tiempo_delta):
    #    if self.vivo:
           
    #        cantidad_movimiento = self.velocidad * tiempo_delta
    #        self.posicion_x = self.posicion_x + (math.cos(self.direccion * math.pi / 180.0) * cantidad_movimiento)
    #        self.posicion_y = self.posicion_y + (math.sin(self.direccion * math.pi / 180.0) * cantidad_movimiento)

    #        if self.posicion_x > 1.05:
    #            self.posicion_x = -1.0
    #        if self.posicion_x < -1.05:
    #            self.posicion_x = 1.0

    #        if self.posicion_y > 1.05:
    #            self.posicion_y = -0.6
    #        if self.posicion_y < -1.0:
    #            self.posicion_y = 1.05
            
            

    def dibujar(self):
        if self.vivo:
            self.shader.usar_programa()
            gl.glBindVertexArray(self.VAO)

            gl.glUniformMatrix4fv(self.transformaciones_id,
                    1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))


                gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

                gl.glBindVertexArray(0)
                self.shader.liberar_programa()   
