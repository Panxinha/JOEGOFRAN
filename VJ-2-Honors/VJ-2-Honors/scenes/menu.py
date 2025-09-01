if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()
    
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
#import scenes.game as GameScene
#import scenes.game_over as DeathScene

pygame.init()
SCREEN_WIDTH= 1000
SCREEN_HEIGHT= 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("VJ-HONORS")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (200, 200, 200)
DARK  = (30, 30, 30)

# Fuente
FONT = pygame.font.SysFont("arial", 36)
SMALL = pygame.font.SysFont("arial", 24)

class Button:
    def __init__(self, text, x, y, w, h, on_click):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.on_click = on_click
        self.hover = False

    def draw(self, surface):
        color = GRAY if self.hover else WHITE
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, DARK, self.rect, 3, border_radius=12)

        txt = FONT.render(self.text, True, BLACK)
        surface.blit(txt, txt.get_rect(center=self.rect.center))

    def update(self, mouse_pos):
        self.hover = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.hover:
            self.on_click()

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.running = True
        self.action = None  # "start", "quit", etc.

        cx = SCREEN_WIDTH // 2
        start_y = 300
        gap = 80
        bw, bh = 300, 60

        # Callbacks definen qué pasa al hacer click
        self.buttons = [
            Button("Jugar",         cx - bw//2, start_y + 0*gap, bw, bh, self._start),
            Button("Instrucciones", cx - bw//2, start_y + 1*gap, bw, bh, self._help),
            Button("Salir",         cx - bw//2, start_y + 2*gap, bw, bh, self._quit),
        ]

        self.bg = pygame.image.load("VJ-2-Honors/assets/menu.png").convert()
        self.bg = pygame.transform.scale(self.bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def _start(self):
        self.action = "start"
        self.running = False

    def _help(self):
        # Muestra un pequeño “modal” con instrucciones sencillas
        self._show_help_popup("- Para moverte utiliza WASD.\n- Para disparar debes hacer click izquierdo.\n- Tu objetivo es eliminar a los enemigos sin morir.\n- Presiona ESC para volver al menú.")

    def _quit(self):
        self.action = "quit"
        self.running = False

    def _show_help_popup(self, text):
        # Pausa la escena y muestra un cuadro con instrucciones hasta que el usuario haga click o presione una tecla
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        lines = text.split("\n")

        popup_w, popup_h = 700, 300
        popup = pygame.Rect((SCREEN_WIDTH - popup_w)//2, (SCREEN_HEIGHT - popup_h)//2, popup_w, popup_h)

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); raise SystemExit
                if event.type == MOUSEBUTTONDOWN:
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

            self.surface.fill(DARK) if self.bg is None else self.surface.blit(self.bg, (0, 0))
            title = FONT.render("Instrucciones", True, WHITE)
            self.surface.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, popup.top - 40)))

            self.surface.blit(overlay, (0, 0))
            pygame.draw.rect(self.surface, WHITE, popup, border_radius=16)
            pygame.draw.rect(self.surface, DARK,  popup, 4, border_radius=16)

            # Dibujar texto dentro del popup
            y = popup.top + 30
            for ln in lines:
                line_surf = SMALL.render(ln, True, BLACK)
                self.surface.blit(line_surf, line_surf.get_rect(center=(SCREEN_WIDTH//2, y)))
                y += 35

            hint = SMALL.render("¡¡Haz click en cualquier parte para continuar!!", True, BLACK)
            self.surface.blit(hint, hint.get_rect(center=(SCREEN_WIDTH//2, popup.bottom - 30)))

            pygame.display.flip()
            clock.tick(60)

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); raise SystemExit
                for b in self.buttons:
                    b.handle_event(event)

            mouse_pos = pygame.mouse.get_pos()
            for b in self.buttons:
                b.update(mouse_pos)

            # Fondo
            if self.bg is None:
                self.surface.fill(DARK)
            else:
                self.surface.blit(self.bg, (0, 0))

            # Título
            title = FONT.render("JORGE vs PROGRAMING BUGS", True, WHITE)
            self.surface.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, 150)))

            # Botones
            for b in self.buttons:
                b.draw(self.surface)

            pygame.display.flip()
            clock.tick(60)

        return self.action

