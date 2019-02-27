# File name: comicwidgets.py
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

# DraggaableWidget class. This class inherits from Relative Layout
class DraggableWidget(RelativeLayout):
	def __init__(self, **kwargs):
		# Attribute that says that the element is not yet selected. Used in select() method
		self.selected = None
		self.touched = False
		super(DraggableWidget, self).__init__(**kwargs)

	# We have to override the three method associated with the touch events.
	# Each of them receives MotionEvent (touch) as a parameter
	def on_touch_down(self, touch):
		# Did the click happened inside the DraggableWidget?
		if self.collide_point(touch.x, touch.y):
			# Do what has to be done
			self.touched = True
			self.select()
			# Indicate the event was procesed
			return True
		# Event outside widget, propagate the event to the children and return the result
		return super(DraggableWidget, self).on_touch_down(touch)

	def select(self):
		# Check that nothing has been selected before
		if not self.selected:
			# Save the center coordinates of the DraggableWidget
			self.ix = self.center_x
			self.iy = self.center_y
			# Dinamically draw a rectangle on its border
			with self.canvas:
				# We kept the Line instance because we have to remove it once the widget is not selected anymore.
				# This is done in the on_touch method
				self.selected = Line(rectangle=(0,0,self.width,self.height), dash_offset=2)

	def on_touch_move(self, touch):
		# Transform widget coordinates to values that are relative to the corresponding parent
		(x,y) = self.parent.to_parent(touch.x, touch.y)
		# Check that the widget is selected. Note we use parent (drawing space) instead of self
		# We also make sure we dont drag the shape outside the drawing space 
		if self.selected and self.parent.collide_point(x - self.width/2, y - self.height/2):
			go = self.parent.general_options
			# Call the translate method
			go.translation = (touch.x - self.ix, touch.y - self.iy)
			#self.translate(touch.x-self.ix,touch.y-self.iy)
			return True
		return super(DraggableWidget, self).on_touch_move(touch)

	def translate(self, x, y):
		self.center_x = self.ix = self.ix + x
		self.center_y = self.iy = self.iy + y

	def on_touch_up(self, touch):
		self.touched = False
		if self.selected:
			if not self.parent.general_options.group_mode:
				self.unselect()
			#return True
		return super(DraggableWidget, self).on_touch_up(touch)

	def unselect(self):
		# Dynamically call the remove method to remove the Line vertex and set out attribute selected to None
		if self.selected:
			self.canvas.remove(self.selected)
			self.selected = None

# Now StickMan inherits from DraggableWidet instead of RelativeLayout
class StickMan(DraggableWidget):
	pass