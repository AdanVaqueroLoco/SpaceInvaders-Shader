from OpenGL.GL import *

import math
from Modelo import *
import glm

class Fondo(Modelo):
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        
        self.vertices=np.array(
           [   
               -0.4,0.85,0,1.0,    1.0,1.0,1.0,
               -0.4,0.84,0,1.0,     1.0,1.0,1.0
           ], dtype="float32"
        ) 
       
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.3,0.45,0,1.0,     1.0,1.0,1.0,
                    0.3,0.46,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.2,0.97,0,1.0,     1.0,1.0,1.0,
                    0.2,0.98,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.2,0.97,0,1.0,     1.0,1.0,1.0,
                    0.2,0.98,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.4,0.17,0,1.0,     1.0,1.0,1.0,
                    0.4,0.18,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.4,-0.47,0,1.0,     1.0,1.0,1.0,
                    0.4,-0.48,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.3,-0.45,0,1.0,     1.0,1.0,1.0,
                    0.3,-0.46,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.1,-0.55,0,1.0,     1.0,1.0,1.0,
                    -0.1,-0.54,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.7,-0.15,0,1.0,     1.0,1.0,1.0,
                    -0.7,-0.14,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.56,-0.98,0,1.0,     1.0,1.0,1.0,
                    -0.56,-0.96,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.52,-0.62,0,1.0,     1.0,1.0,1.0,
                    -0.52,-0.6,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.87,-0.93,0,1.0,     1.0,1.0,1.0,
                    -0.87,-0.95,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.82,-0.33,0,1.0,     1.0,1.0,1.0,
                    0.82,-0.34,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.1,-0.23,0,1.0,     1.0,1.0,1.0,
                    0.1,-0.24,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.2,-0.53,0,1.0,     1.0,1.0,1.0,
                    0.2,-0.54,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.8,-0.32,0,1.0,     1.0,1.0,1.0,
                    0.82,-0.34,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.86,-0.12,0,1.0,     1.0,1.0,1.0,
                    0.86,-0.13,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.31,-0.22,0,1.0,     1.0,1.0,1.0,
                    -0.31,-0.23,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.23,-0.26,0,1.0,     1.0,1.0,1.0,
                    0.23,-0.26,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.0,-0.56,0,1.0,     1.0,1.0,1.0,
                    0.0,-0.54,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.1,-0.52,0,1.0,     1.0,1.0,1.0,
                    0.1,-0.53,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.23,-0.15,0,1.0,     1.0,1.0,1.0,
                    -0.23,-0.16,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.93,0.43,0,1.0,     1.0,1.0,1.0,
                    -0.93,0.44,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.46,0.42,0,1.0,     1.0,1.0,1.0,
                    -0.46,0.43,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.23,0.86,0,1.0,     1.0,1.0,1.0,
                    -0.23,0.87,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.42,-0.15,0,1.0,     1.0,1.0,1.0,
                    -0.42,-0.16,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.93,0.43,0,1.0,     1.0,1.0,1.0,
                    -0.93,0.44,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.46,0.42,0,1.0,     1.0,1.0,1.0,
                    -0.46,0.43,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.23,0.86,0,1.0,     1.0,1.0,1.0,
                    0.23,0.87,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.32,-0.9,0,1.0,     1.0,1.0,1.0,
                    0.32,-0.91,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.4,0.3,0,1.0,     1.0,1.0,1.0,
                    0.4,0.33,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.7,0.4,0,1.0,     1.0,1.0,1.0,
                    -0.7,0.3,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.8,0.35,0,1.0,     1.0,1.0,1.0,
                    -0.6,0.35,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.75,0.33,0,1.0,     1.0,1.0,1.0,
                    -0.65,0.37,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.2,0.05,0,1.0,     1.0,1.0,1.0,
                    -0.2,0.06,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.26,0.15,0,1.0,     1.0,1.0,1.0,
                    -0.26,0.15,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.3,0.37,0,1.0,     1.0,1.0,1.0,
                    0.3,0.36,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.35,0.1,0,1.0,     1.0,1.0,1.0,
                    -0.35,0.1,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.7,-0.4,0,1.0,     1.0,1.0,1.0,
                    0.7,-0.3,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.8,-0.35,0,1.0,     1.0,1.0,1.0,
                    0.6,-0.35,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.75,-0.33,0,1.0,     1.0,1.0,1.0,
                    0.65,-0.37,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.75,-0.37,0,1.0,     1.0,1.0,1.0,
                    0.65,-0.33,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    0.9,-0.7,0,1.0,     1.0,1.0,1.0,
                    0.9,-0.6,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )

        self.vertices = np.append(self.vertices, np.array(
                [
                    1.0,-0.65,0,1.0,     1.0,1.0,1.0,
                    0.8,-0.65,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.95,-0.67,0,1.0,     1.0,1.0,1.0,
                    0.85,-0.63,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.6,0.7,0,1.0,     1.0,1.0,1.0,
                    -0.6,0.71,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.7,0.55,0,1.0,     1.0,1.0,1.0,
                    -0.7,0.54,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        self.vertices = np.append(self.vertices, np.array(
                [
                    0.8,0.65,0,1.0,     1.0,1.0,1.0,
                    0.8,0.64,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        
        self.vertices = np.append(self.vertices, np.array(
                [
                    -0.1,0.75,0,1.0,     1.0,1.0,1.0,
                    -0.1,0.74,0,1.0,     1.0,1.0,1.0
                    
                ], dtype="float32"
            )
        )
        
        self.transformaciones = glm.mat4(1.0)
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 2, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 6, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 10, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 14, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 18, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 22, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 26, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 30, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 34, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 38, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 42, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 46, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 50, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 54, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 58, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 62, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 66, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 68, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 70, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 72, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 74, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 76, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 78, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 80, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 82, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 84, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 86, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 88, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 90, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 92, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 94, 2)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 96, 2)
        
        gl.glBindVertexArray(0)
        self.shader.liberar_programa()

    def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)