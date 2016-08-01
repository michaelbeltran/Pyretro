import pygame, random, sys
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

RIGHT = 275
LEFT = 276
UP = 273
DOWN = 274
class Snake(object):
	def __init__(self):
		self.width = 600
		self.height = 600
		self.s_siz = 4
		self.s_x = 300
		self.s_y = 300
		self.s_dir = LEFT
		self.sp = 5
		self.temp_r = []
		self.f = pygame.Rect(200,200,5,5)
		self.size = (self.width+2, self.height+2)
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Snake")
		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self.direction(event.dict['key'])
			self.screen.fill(BLACK)
			self.game()
			pygame.display.update()
			pygame.time.delay(50)
	def x_p(self):
		return random.randint(21, self.width-23)
	def y_p(self):
		return random.randint(21, self.height-23)
	def game(self):
		self.frame()
		self.snake()
		self.food()
	def food(self):
		if self.s_h.colliderect(self.f):
			self.f = pygame.Rect(self.x_p(), self.y_p(), 5, 5)
			self.s_siz +=1
		pygame.draw.rect(self.screen, GREEN, self.f)
	def snake(self):
		rect = []
		if self.s_dir == RIGHT:
			self.s_x += self.sp 
		elif self.s_dir == LEFT:
			self.s_x -= self.sp
		elif self.s_dir == UP:
			self.s_y -= self.sp
		elif self.s_dir == DOWN:
			self.s_y += self.sp
		if len(self.temp_r) == 0:
			for i in range(self.s_siz):
				rect.append( pygame.Rect(self.s_x+(i*5), self.s_y, 5, 5))
		else:
			for i in range(self.s_siz):
				if i == 0:
					rect.append(pygame.Rect(self.s_x, self.s_y, 5, 5))
				else:
					rect.append(self.temp_r[i-1])
		self.temp_r = rect
		self.s_h = rect[0]
		for i in range(self.s_siz):
			pygame.draw.rect(self.screen, GREEN, rect[i])
		if rect[0].x == 5 or rect[0].x == self.width or\
			rect[0].y == 5 or rect[0].y == self.height:
			sys.exit()
					
	def direction(self, key):
		if key == UP:
			self.s_dir = UP
		elif key == DOWN:
			self.s_dir = DOWN
		elif key == RIGHT:
			self.s_dir = RIGHT
		elif key == LEFT:
			self.s_dir = LEFT
	def frame(self):
		point = ( (0,0), (0, self.width),
				(0, self.width), (self.width, self.height),
				(self.width, self.height), (self.width, 0)
		)
		pygame.draw.lines(self.screen, GREEN, True, point, 20)

def main():
	snake = Snake()

if __name__ == "__main__":
	main()
