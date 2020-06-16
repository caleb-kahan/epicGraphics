
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS DISPLAY DOUBLE DRAWSHAPE EXTRUSION FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE LIST_TUPLES MESH MOVE PLANE POP PUSH REVOLUTION ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SHAPE SPHERE STRING TEXTURE TORUS TRUNCATION TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEPOINTLIST : LIST_TUPLEScommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : SHAPE SYMBOL PLANE POINTLIST NUMBER NUMBER NUMBERcommand : DRAWSHAPE SYMBOLcommand : EXTRUSION SYMBOL SYMBOL NUMBERcommand : REVOLUTION SYMBOL SYMBOL XYZ NUMBERcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,30,36,38,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[-1,0,-1,-3,-10,-11,-13,-15,-57,-66,-2,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'COMMENT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[3,3,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'POP':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[4,4,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'PUSH':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[5,5,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SCREEN':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[6,6,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SAVE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[7,7,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'DISPLAY':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[8,8,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SPHERE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[9,9,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'TORUS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[10,10,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'BOX':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[11,11,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SHAPE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[12,12,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'DRAWSHAPE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[13,13,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'EXTRUSION':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[14,14,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'REVOLUTION':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[15,15,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'LINE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[16,16,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'MOVE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[17,17,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SCALE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[18,18,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'ROTATE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[19,19,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'FRAMES':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[20,20,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'BASENAME':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[21,21,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'VARY':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[22,22,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SET':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[23,23,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SET_KNOBS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[24,24,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'AMBIENT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[25,25,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'CONSTANTS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[26,26,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'LIGHT':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[27,27,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SHADING':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[28,28,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'CAMERA':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[29,29,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[30,30,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'MESH':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[31,31,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[32,32,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'SAVE_COORDS':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[33,33,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'TWEEN':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[34,34,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'FOCAL':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[35,35,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'WEB':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[36,36,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'TEXTURE':([0,2,3,4,5,6,8,30,36,40,42,43,44,45,53,61,62,65,69,73,74,76,78,79,93,95,100,112,116,117,118,120,124,125,128,135,139,140,145,146,148,149,150,159,164,165,166,167,169,170,176,178,179,180,181,182,184,186,188,189,190,191,194,197,203,204,],[37,37,-3,-10,-11,-13,-15,-57,-66,-8,-6,-7,-4,-5,-29,-46,-47,-50,-55,-62,-63,-65,-12,-14,-45,-49,-58,-30,-41,-43,-44,-51,-60,-59,-16,-31,-40,-42,-61,-64,-18,-17,-20,-48,-19,-21,-22,-24,-28,-32,-56,-23,-25,-26,-33,-34,-36,-54,-27,-35,-38,-37,-39,-52,-53,-67,]),'DOUBLE':([6,9,10,11,16,17,18,20,24,25,29,34,35,39,40,44,45,46,47,48,49,50,51,56,57,58,59,60,63,64,66,67,68,70,75,77,80,81,82,83,84,85,87,89,90,91,92,94,96,97,98,99,103,104,105,106,107,108,109,110,111,113,114,115,119,121,122,123,127,129,130,131,132,133,134,136,137,138,141,142,143,144,147,151,152,153,154,155,156,157,158,160,161,162,163,168,171,172,173,174,175,177,183,185,187,192,193,195,196,197,198,199,200,201,202,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,-8,-4,-5,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-9,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'STRING':([7,21,41,42,43,44,45,71,101,],[43,43,43,-6,-7,-4,-5,43,43,]),'XYZ':([7,9,10,11,12,13,14,15,16,19,21,22,23,26,27,31,32,33,37,40,41,42,43,44,45,54,55,71,88,93,100,101,102,114,116,117,125,126,128,138,149,150,166,167,170,180,182,184,190,],[44,44,44,44,44,44,44,44,44,60,44,44,44,44,44,44,44,44,44,-8,44,-6,-7,-4,-5,44,44,44,113,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ID':([7,9,10,11,12,13,14,15,16,21,22,23,26,27,31,32,33,37,40,41,42,43,44,45,54,55,71,93,100,101,102,114,116,117,125,126,128,138,149,150,166,167,170,180,182,184,190,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-8,45,-6,-7,-4,-5,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'SHADING_TYPE':([28,],[69,]),'CO':([31,44,45,72,],[71,-4,-5,101,]),'PLANE':([44,45,52,],[-4,-5,86,]),'LIST_TUPLES':([86,],[111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,38,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,16,17,18,20,24,25,29,34,35,39,46,47,48,49,50,51,56,57,58,59,60,63,64,66,67,68,70,75,77,80,81,82,83,84,85,87,89,90,91,92,94,96,97,98,99,103,104,105,106,107,108,109,110,113,114,115,119,121,122,123,127,129,130,131,132,133,134,136,137,138,141,142,143,144,147,151,152,153,154,155,156,157,158,160,161,162,163,168,171,172,173,174,175,177,183,185,187,192,193,195,196,197,198,199,200,201,202,],[39,46,48,50,56,58,59,61,65,66,70,75,76,78,80,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,102,103,104,105,106,107,108,109,112,114,115,116,117,119,120,121,122,123,127,128,129,130,131,132,133,134,135,136,138,141,142,143,144,147,149,150,151,152,153,154,155,156,158,159,160,161,162,163,166,167,168,169,170,171,172,173,174,175,176,177,180,182,183,184,185,186,187,190,192,193,195,196,197,198,199,200,201,202,203,204,]),'TEXT':([7,21,41,71,101,],[41,62,79,100,125,]),'SYMBOL':([7,9,10,11,12,13,14,15,16,21,22,23,26,27,31,32,33,37,41,54,55,71,93,100,101,102,114,116,117,125,126,128,138,149,150,166,167,170,180,182,184,190,],[42,47,49,51,52,53,54,55,57,42,63,64,67,68,72,73,74,77,42,87,88,42,118,124,42,126,137,139,140,145,146,148,157,164,165,178,179,181,188,189,191,194,]),'POINTLIST':([86,],[110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',143),
  ('input -> command input','input',2,'p_input','mdl.py',144),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',148),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',152),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',153),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',157),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',158),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',162),
  ('POINTLIST -> LIST_TUPLES','POINTLIST',1,'p_POINTLIST','mdl.py',166),
  ('command -> POP','command',1,'p_command_stack','mdl.py',170),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',171),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',175),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',176),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',183),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',187),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',191),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',192),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',193),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',194),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',208),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',209),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',210),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',211),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',225),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',226),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',227),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',228),
  ('command -> SHAPE SYMBOL PLANE POINTLIST NUMBER NUMBER NUMBER','command',7,'p_command_shape','mdl.py',242),
  ('command -> DRAWSHAPE SYMBOL','command',2,'p_command_drawshape','mdl.py',248),
  ('command -> EXTRUSION SYMBOL SYMBOL NUMBER','command',4,'p_command_extrusion','mdl.py',253),
  ('command -> REVOLUTION SYMBOL SYMBOL XYZ NUMBER','command',5,'p_command_revolution','mdl.py',258),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',263),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',264),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',265),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',266),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',267),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',268),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',269),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',270),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',291),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',292),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',300),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',301),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',309),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',310),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',318),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',323),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',328),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',334),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',335),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',346),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',352),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',353),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',359),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',365),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',371),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',376),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',380),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',381),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',382),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',383),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',397),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',403),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',410),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',415),
  ('command -> WEB','command',1,'p_web','mdl.py',419),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',423),
]