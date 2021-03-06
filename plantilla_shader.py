import OpenGL.GL as gl
import glfw
import numpy as np

from Shader import *
from Modelo import *
from Triangulo import Triangulo
from Fondo import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

invasor_uno = None
invasor_dos = None
invasor_tres = None
invasor_cuatro = None
invasor_cinco = None
fondo = None
modelo = None
window = None

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global window
    global tiempo_anterior
    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    estado_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    if estado_arriba == glfw.PRESS:
        modelo.mover(modelo.ARRIBA, tiempo_delta)
    if estado_abajo == glfw.PRESS:
        modelo.mover(modelo.ABAJO, tiempo_delta)
    if estado_derecha == glfw.PRESS:
        modelo.mover(modelo.DERECHA, tiempo_delta)
    if estado_izquierda == glfw.PRESS:
        modelo.mover(modelo.IZQUIERDA, tiempo_delta)

    if invasor_cinco.colisionando(modelo):
            bicho.vivo = False
    if invasor_cuatro.colisionando(modelo):
            bicho2.vivo = False
    if invasor_tres.colisionando(modelo):
            bicho3.vivo = False
    if invasor_dos.colisionando(modelo):
            bicho4.vivo = False
    if invasor_uno.colisionando(modelo):
            bicho5.vivo = False

    if ((invasor_uno.vivo == False) & (invasor_dos.vivo == False) & (invasor_tres.vivo == False) & (invasor_cuatro.vivo == False) & (invasor_cinco.vivo == False)):
        glfw.set_window_should_close(window, 1)
        print("Game over: ganaste")

    if modelo.colisionando(powerUp):
        modelo.velocidad = modelo.velocidad = 1.6

    tiempo_anterior=tiempo_actual

def colisionando():
    colisionando=False
    return colisionando

def dibujar():
    global modelo
    global invasor_uno
    global invasor_dos
    global invasor_tres
    global invasor_cuatro
    global invasor_cinco
    global fondo 
    fondo.dibujar()
    modelo.dibujar()
    invasor_uno.dibujar()
    invasor_dos.dibujar()
    invasor_tres.dibujar()
    invasor_cuatro.dibujar()
    invasor_cinco.dibujar()

def main():
    global modelo
    global fondo
    global window
    global invasor_uno
    global invasor_dos
    global invasor_tres
    global invasor_cuatro
    global invasor_cinco
    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Plantilla Shaders",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")

    fondo = Fondo(shader,
            posicion_id, color_id, transformaciones_id)

    modelo = Triangulo(shader, 
            posicion_id, color_id, transformaciones_id)

    invasor_cinco = invasor_cinco(shader, posicion_id, color_id, transformaciones_id)
    invasor_cuatro = invasor_cuatro(shader, posicion_id, color_id, transformaciones_id)
    invasor_tres = invasor_tres(shader, posicion_id, color_id, transformaciones_id)
    invasor_dos = invasor_dos(shader, posicion_id, color_id, transformaciones_id)
    invasor_uno = invasor_uno(shader, posicion_id, color_id, transformaciones_id)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(0.1,0.1,0.1,1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    fondo.borrar()
    shader.borrar()
    invasor_cinco.borrar()
    invasor_cuatro.borrar()
    invasor_tres.borrar()
    invasor_dos.borrar()
    invasor_uno.borrar()

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)


if __name__ == '__main__':
    main()