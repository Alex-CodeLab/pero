#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import modules
import json
from ...enums import *
from ...colors import Color
from ...properties import UNDEF
from ...drawing import Canvas


class JsonCanvas(Canvas):
    """Wrapper for buffered JSON drawing context."""
    
    
    def __init__(self, **overrides):
        """Initializes a new instance of JsonCanvas."""
        
        # init buffers
        self._commands = []
        
        # init base
        super(JsonCanvas, self).__init__()
        
        # bind events
        self.bind(EVENT.PROPERTY_CHANGED, self._on_json_property_changed)
        
        # set overrides
        self.set_properties(overrides)
    
    
    def set_viewport(self, x=None, y=None, width=None, height=None, relative=False):
        """
        Sets rectangular region currently used for drawing. This provides an
        easy way to draw complex graphics at specific position of the
        canvas without adjusting the coordinates of the graphics. It is achieved
        by changing the origin coordinates and the logical width and height of
        the canvas.
        
        Args:
            x: int or float
                X-coordinate of the top-left corner.
            
            y: int or float
                Y-coordinate of the top-left corner.
            
            width: int, float or None
                Full width of the viewport.
            
            height: int, float or None
                Full height of the viewport.
            
            relative: bool
                If set to True the new viewport is applied relative to current
                one.
        """
        
        # set to base
        super(JsonCanvas, self).set_viewport(x, y, width, height, relative)
        
        # store command
        self._store_command('set_viewport', {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'relative': relative})
    
    
    def get_json(self):
        """
        Gets JSON string for current drawings.
        
        Returns:
            str
                Drawings JSON string.
        """
        
        return json.dumps({"commands": self._commands})
    
    
    def draw_arc(self, x, y, radius, start_angle, end_angle, clockwise=True):
        """
        Draws an arc of specified radius centered around given coordinates.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            radius: int or float
                Radius of the arc.
            
            start_angle: int or float
                Angle of the starting point in radians.
            
            end_angle: int or float
                Angle of the starting point in radians.
            
            clockwise: bool
                Direction of drawing between start and end point.
        """
        
        # store command
        self._store_command('draw_arc', {
            'x': x,
            'y': y,
            'radius': radius,
            'start_angle': start_angle,
            'end_angle': end_angle,
            'clockwise': clockwise})
    
    
    def draw_circle(self, x, y, radius):
        """
        Draws a circle of specified radius centered around given coordinates.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            radius: int or float
                Radius of the circle.
        """
        
        # store command
        self._store_command('draw_circle', {
            'x': x,
            'y': y,
            'radius': radius})
    
    
    def draw_ellipse(self, x, y, width, height):
        """
        Draws an ellipse centered around given coordinates and fitting into the
        width and height.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            width: int or float
                Full width of the ellipse.
            
            height: int or float
                Full height of the ellipse.
        """
        
        # store command
        self._store_command('draw_ellipse', {
            'x': x,
            'y': y,
            'width': width,
            'height': height})
    
    
    def draw_line(self, x1, y1, x2, y2):
        """
        Draws a line between two points.
        
        Args:
            x1: int or float
                X-coordinate of the line start.
            
            y1: int or float
                Y-coordinate of the line start.
            
            x2: int or float
                X-coordinate of the line end.
            
            y2: int or float
                Y-coordinate of the line end.
        """
        
        # store command
        self._store_command('draw_line', {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2})
    
    
    def draw_lines(self, points):
        """
        Draws continuous open line using sequence of points.
        
        Args:
            points: ((float, float),)
                Sequence of x,y coordinates of the points.
        """
        
        # disconnect points
        points = tuple((p[0], p[1]) for p in points)
        
        # store command
        self._store_command('draw_lines', {'points': points})
    
    
    def draw_path(self, path):
        """
        Draws given path using current pen and brush.
        
        Args:
            path: pero.Path
                Path to be drawn.
        """
        
        # get path dump
        path = json.loads(path.json())
        
        # store command
        self._store_command('draw_path', {'path': path})
    
    
    def draw_polygon(self, points):
        """
        Draws a closed polygon using sequence of points.
        
        Args:
            points: ((float, float),)
                Sequence of x,y coordinates of the points.
        """
        
        # disconnect points
        points = tuple((p[0], p[1]) for p in points)
        
        # store command
        self._store_command('draw_polygon', {'points': points})
    
    
    def draw_rect(self, x, y, width, height, radius=None):
        """
        Draws a rectangle specified by given top left corner and size and
        optional round corners specified as a single value or individual value
        for each corners starting from top-left.
        
        Args:
            x: int or float
                X-coordinate of the center.
            
            y: int or float
                Y-coordinate of the center.
            
            width: int or float
                Full width of the rectangle.
            
            height: int or float
                Full height of the rectangle.
            
            radius: int, float, (int,int,int,int) or (float,float,float,float)
                Radius of curved corners.
        """
        
        # store command
        self._store_command('draw_rect', {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'radius': radius})
    
    
    def draw_text(self, text, x, y, angle=0):
        """
        Draws a text string anchored at specified point using current text
        settings.
        
        Args:
            text: str
                Text to be drawn.
            
            x: int or float
                X-coordinate of the text anchor.
            
            y: int or float
                Y-coordinate of the text anchor.
            
            angle: int or float
                Text angle in radians.
        """
        
        # store command
        self._store_command('draw_text', {
            'text': text,
            'x': x,
            'y': y,
            'angle': angle})
    
    
    def fill(self):
        """Fills current drawing region by actual fill color."""
        
        # store command
        self._store_command('fill')
    
    
    def clip(self, path):
        """
        Sets clipping path as intersection with current one.
        
        Args:
            path: pero.Path
                Path to be used for clipping.
        """
        
        # get path dump
        path = json.loads(path.json())
        
        # store command
        self._store_command('clip', {'path': path})
    
    
    def unclip(self):
        """Removes last clipping path while keeping previous if any."""
        
        # store command
        self._store_command('unclip')
    
    
    def group(self, id_tag=None, class_tag=None):
        """
        Opens new drawing group.
        
        Args:
            id_tag: str
                Unique id of the group.
            
            class_tag:
                Class of the group.
        """
        
        # store command
        self._store_command('group', {
            'id_tag': id_tag,
            'class_tag': class_tag})
    
    
    def ungroup(self):
        """Closes the last drawing group."""
        
        # store command
        self._store_command('ungroup')
    
    
    def _store_command(self, command, args=None):
        """Stores command and its parameters."""
        
        if args is None:
            args = {}
        
        self._commands.append((command, args))
    
    
    def _on_json_property_changed(self, evt):
        """Called after any property has changed."""
        
        # get value
        value = evt.new_value
        
        # convert UNDEF
        if value is UNDEF:
            value = str(UNDEF)
        
        # convert color
        elif isinstance(value, Color):
            value = value.hex
        
        # store command
        self._store_command('set_property', {
            'name': evt.name,
            'value': value,
            'raise_error': False})