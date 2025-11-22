import pygame
import sys

from screens.base_screen import BaseScreen

class RankingScreen(BaseScreen):
    def __init__(self, screen, width=800, height=600):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
    def run(self):
        clock = pygame.time.Clock()
        while True:
            mouse_click_pos = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return "menu"

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_click_pos = event.pos

            # desenha a tela
            self.draw()

            # processa clique após desenhar (button_rect é definido em draw)
            if mouse_click_pos and getattr(self, 'button_rect', None):
                if self.button_rect.collidepoint(mouse_click_pos):
                    return "menu"

            pygame.display.flip()
            clock.tick(60)

    def draw(self):
        self.screen.fill((30, 30, 30))

        # Título
        title_surface = self.title_font.render("RANKING", True, (255, 255, 255))
        self.screen.blit(title_surface, (self.width // 2 - title_surface.get_width() // 2, 50))

        # Quadro para ranking
        panel_rect = pygame.Rect(self.width // 2 - 250, 150, 500, 300)
        pygame.draw.rect(self.screen, (50, 50, 50), panel_rect, border_radius=15)
        pygame.draw.rect(self.screen, (255, 255, 255), panel_rect, 3, border_radius=15)

        # Texto placeholder
        placeholder = self.font_text.render("Nenhum dado disponível.", True, (200, 200, 200))
        self.screen.blit(placeholder, (self.width // 2 - placeholder.get_width() // 2, 300))

        # Botão voltar
        self.button_rect = pygame.Rect(self.width // 2 - 100, 480, 200, 55)
        pygame.draw.rect(self.screen, (90, 90, 90), self.button_rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), self.button_rect, 2, border_radius=10)

        button_text = self.button_font.render("Voltar", True, (255, 255, 255))
        self.screen.blit(button_text, (
            self.button_rect.centerx - button_text.get_width() // 2,
            self.button_rect.centery - button_text.get_height() // 2
        ))