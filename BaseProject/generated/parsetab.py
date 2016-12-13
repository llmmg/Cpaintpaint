
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'FD6D3FF64960156BC42A6ECE78C9F2EA'
    
_lr_action_items = {'=':([5,],[16,]),'(':([2,4,7,9,11,12,16,22,23,26,33,35,37,],[9,11,11,11,11,11,11,11,11,11,11,11,11,]),'{':([13,14,17,21,27,28,29,],[-10,-11,25,-13,-12,-9,-8,]),'NUMBER':([4,7,9,11,12,16,22,23,26,33,35,37,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'PRINT':([0,10,25,],[4,4,4,]),'IDENTIFIER':([0,4,7,9,10,11,12,16,22,23,25,26,33,35,37,],[5,14,14,14,5,14,14,14,14,14,5,14,14,14,14,]),';':([1,3,8,13,14,15,21,24,27,28,29,32,39,],[-3,10,-4,-10,-11,-5,-13,-14,-12,-9,-8,-6,-7,]),'MUL_OP':([13,14,15,17,18,20,21,24,27,28,29,31,34,36,38,],[-10,-11,22,22,22,22,-13,22,-12,-9,22,22,22,22,22,]),'ADD_OP':([4,7,9,11,12,13,14,15,16,17,18,20,21,22,23,24,26,27,28,29,31,33,34,35,36,37,38,],[12,12,12,12,12,-10,-11,23,12,23,23,23,-13,12,12,23,12,-12,-9,-8,23,12,23,12,23,12,23,]),'WHILE':([0,10,25,],[7,7,7,]),'PRINTPIXEL':([0,10,25,],[2,2,2,]),'}':([1,3,8,13,14,15,19,21,24,27,28,29,30,32,39,],[-3,-1,-4,-10,-11,-5,-2,-13,-14,-12,-9,-8,32,-6,-7,]),'$end':([1,3,6,8,13,14,15,19,21,24,27,28,29,32,39,],[-3,-1,0,-4,-10,-11,-5,-2,-13,-14,-12,-9,-8,-6,-7,]),',':([13,14,18,21,27,28,29,31,34,36,],[-10,-11,26,-13,-12,-9,-8,33,35,37,]),')':([13,14,20,21,27,28,29,38,],[-10,-11,27,-13,-12,-9,-8,39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([4,7,9,11,12,16,22,23,26,33,35,37,],[15,17,18,20,21,24,28,29,31,34,36,38,]),'assignation':([0,10,25,],[1,1,1,]),'statement':([0,10,25,],[3,3,3,]),'programme':([0,10,25,],[6,19,30,]),'structure':([0,10,25,],[8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parserPaint.py',9),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parserPaint.py',14),
  ('statement -> assignation','statement',1,'p_statement','parserPaint.py',19),
  ('statement -> structure','statement',1,'p_statement','parserPaint.py',20),
  ('statement -> PRINT expression','statement',2,'p_statement_print','parserPaint.py',25),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure','parserPaint.py',30),
  ('statement -> PRINTPIXEL ( expression , expression , expression , expression , expression )','statement',12,'p_printPixel','parserPaint.py',35),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parserPaint.py',40),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parserPaint.py',41),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_var','parserPaint.py',46),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parserPaint.py',47),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parserPaint.py',52),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parserPaint.py',57),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parserPaint.py',62),
]
