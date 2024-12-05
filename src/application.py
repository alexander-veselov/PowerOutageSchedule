import pygame
from data import request_power_outage_data

def print_debug_data(address: str):
    power_outage_data = request_power_outage_data(address)
    if power_outage_data.current.hasQueue == 'yes':
        today = power_outage_data.graphs.today
        if today is not None:
            for hour in today.hoursList:
                print(hour)

class Application:
    def __init__(self, address: str, width: int, height: int):
        pygame.init()
        pygame.display.set_caption('Power Outage Schedule')
        self.running = False
        self.address = address
        self.surface = pygame.display.set_mode((width, height))

    def run(self):
        # TODO: remove
        print_debug_data(self.address)

        self.running = True
        while self.running:
            self.process_events(pygame.event.get())
            self.render()

    def close(self):
        self.running = False

    def process_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.close()
    
    def render(self):
        pygame.display.flip()

