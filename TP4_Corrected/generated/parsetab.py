
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '2E6180939D9388C4833E31478CA02687'
    
_lr_action_items = {'NUMBER':([3,5,10,11,15,20,21,],[9,9,9,9,9,9,9,]),')':([9,12,17,18,23,25,26,],[-9,-10,-12,23,-11,-7,-8,]),'(':([3,5,10,11,15,20,21,],[11,11,11,11,11,11,11,]),'WHILE':([0,8,19,],[3,3,3,]),'PRINT':([0,8,19,],[5,5,5,]),'{':([9,12,13,17,23,25,26,],[-9,-10,19,-12,-11,-7,-8,]),';':([1,4,6,9,12,14,17,22,23,25,26,27,],[8,-4,-3,-9,-10,-5,-12,-13,-11,-7,-8,-6,]),'=':([7,],[15,]),'ADD_OP':([3,5,9,10,11,12,13,14,15,17,18,20,21,22,23,25,26,],[10,10,-9,10,10,-10,20,20,10,-12,20,10,10,20,-11,-7,-8,]),'IDENTIFIER':([0,3,5,8,10,11,15,19,20,21,],[7,12,12,7,12,12,12,7,12,12,]),'}':([1,4,6,9,12,14,16,17,22,23,24,25,26,27,],[-1,-4,-3,-9,-10,-5,-2,-12,-13,-11,27,-7,-8,-6,]),'MUL_OP':([9,12,13,14,17,18,22,23,25,26,],[-9,-10,21,21,-12,21,21,-11,21,-8,]),'$end':([1,2,4,6,9,12,14,16,17,22,23,25,26,27,],[-1,0,-4,-3,-9,-10,-5,-2,-12,-13,-11,-7,-8,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'structure':([0,8,19,],[4,4,4,]),'statement':([0,8,19,],[1,1,1,]),'programme':([0,8,19,],[2,16,24,]),'expression':([3,5,10,11,15,20,21,],[13,14,17,18,22,25,26,]),'assignation':([0,8,19,],[6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_programme_statement','parser5.py',9),
  ('programme -> statement ; programme','programme',3,'p_programme_recursive','parser5.py',13),
  ('statement -> assignation','statement',1,'p_statement','parser5.py',17),
  ('statement -> structure','statement',1,'p_statement','parser5.py',18),
  ('statement -> PRINT expression','statement',2,'p_statement_print','parser5.py',22),
  ('structure -> WHILE expression { programme }','structure',5,'p_structure','parser5.py',26),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser5.py',30),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parser5.py',31),
  ('expression -> NUMBER','expression',1,'p_expression_num_or_var','parser5.py',35),
  ('expression -> IDENTIFIER','expression',1,'p_expression_num_or_var','parser5.py',36),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parser5.py',40),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parser5.py',44),
  ('assignation -> IDENTIFIER = expression','assignation',3,'p_assign','parser5.py',48),
]