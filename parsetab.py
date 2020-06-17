
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS DISPLAY DOUBLE EXTRUSION FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE LIST_TUPLES MESH MOVE PLANE POP PRINT PUSH REVOLUTION ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SHAPE SPHERE STRING TEXTURE TORUS TRUNCATION TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEPOINTLIST : LIST_TUPLEScommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : SHAPE SYMBOL PLANE POINTLISTcommand : EXTRUSION SYMBOL SYMBOL NUMBERcommand : REVOLUTION SYMBOL SYMBOL XYZ NUMBERcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : PRINT TEXT\n               | PRINTcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,29,35,36,38,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[-1,0,-1,-3,-10,-11,-13,-15,-56,-65,-67,-2,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'COMMENT':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[3,3,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'POP':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[4,4,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'PUSH':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[5,5,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SCREEN':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[6,6,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SAVE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[7,7,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'DISPLAY':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[8,8,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SPHERE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[9,9,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'TORUS':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[10,10,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'BOX':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[11,11,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SHAPE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[12,12,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'EXTRUSION':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[13,13,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'REVOLUTION':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[14,14,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'LINE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[15,15,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'MOVE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[16,16,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SCALE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[17,17,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'ROTATE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[18,18,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'FRAMES':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[19,19,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'BASENAME':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[20,20,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'VARY':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[21,21,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SET':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[22,22,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SET_KNOBS':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[23,23,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'AMBIENT':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[24,24,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'CONSTANTS':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[25,25,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'LIGHT':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[26,26,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SHADING':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[27,27,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'CAMERA':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[28,28,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[29,29,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'MESH':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[30,30,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[31,31,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'SAVE_COORDS':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[32,32,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'TWEEN':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[33,33,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'FOCAL':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[34,34,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'WEB':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[35,35,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'PRINT':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[36,36,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'TEXTURE':([0,2,3,4,5,6,8,29,35,36,40,42,43,44,45,60,61,64,68,72,73,75,76,78,79,93,95,100,110,111,112,116,117,118,120,124,125,128,134,138,139,144,145,147,148,149,157,162,163,164,165,167,173,175,176,177,178,179,181,183,185,186,187,188,191,194,200,201,],[37,37,-3,-10,-11,-13,-15,-56,-65,-67,-8,-6,-7,-4,-5,-45,-46,-49,-54,-61,-62,-64,-66,-12,-14,-44,-48,-57,-28,-9,-29,-40,-42,-43,-50,-59,-58,-16,-30,-39,-41,-60,-63,-18,-17,-20,-47,-19,-21,-22,-24,-31,-55,-23,-25,-26,-32,-33,-35,-53,-27,-34,-37,-36,-38,-51,-52,-68,]),'DOUBLE':([6,9,10,11,15,16,17,19,23,24,28,33,34,39,40,44,45,46,47,48,49,50,51,55,56,57,58,59,62,63,65,66,67,69,74,77,80,81,82,83,84,85,87,89,90,91,92,94,96,97,98,99,103,104,105,106,107,108,109,113,114,115,119,121,122,123,127,129,130,131,132,133,135,136,137,140,141,142,143,146,150,151,152,153,154,155,156,158,159,160,161,166,168,169,170,171,172,174,180,182,184,189,190,192,193,194,195,196,197,198,199,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,-8,-4,-5,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'STRING':([7,20,36,41,42,43,44,45,70,101,],[43,43,43,43,-6,-7,-4,-5,43,43,]),'XYZ':([7,9,10,11,12,13,14,15,18,20,21,22,25,26,30,31,32,36,37,40,41,42,43,44,45,53,54,70,88,93,100,101,102,114,116,117,125,126,128,137,148,149,164,165,167,177,179,181,187,],[44,44,44,44,44,44,44,44,59,44,44,44,44,44,44,44,44,44,44,-8,44,-6,-7,-4,-5,44,44,44,113,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ID':([7,9,10,11,12,13,14,15,20,21,22,25,26,30,31,32,36,37,40,41,42,43,44,45,53,54,70,93,100,101,102,114,116,117,125,126,128,137,148,149,164,165,167,177,179,181,187,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-8,45,-6,-7,-4,-5,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'SHADING_TYPE':([27,],[68,]),'CO':([30,44,45,71,],[70,-4,-5,101,]),'PLANE':([44,45,52,],[-4,-5,86,]),'LIST_TUPLES':([86,],[111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,38,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,15,16,17,19,23,24,28,33,34,39,46,47,48,49,50,51,55,56,57,58,59,62,63,65,66,67,69,74,77,80,81,82,83,84,85,87,89,90,91,92,94,96,97,98,99,103,104,105,106,107,108,109,113,114,115,119,121,122,123,127,129,130,131,132,133,135,136,137,140,141,142,143,146,150,151,152,153,154,155,156,158,159,160,161,166,168,169,170,171,172,174,180,182,184,189,190,192,193,194,195,196,197,198,199,],[39,46,48,50,55,57,58,60,64,65,69,74,75,78,80,81,82,83,84,85,89,90,91,92,93,94,95,96,97,98,99,102,103,104,105,106,107,108,109,112,114,115,116,117,119,120,121,122,123,127,128,129,130,131,132,133,134,135,137,140,141,142,143,146,148,149,150,151,152,153,154,156,157,158,159,160,161,164,165,166,167,168,169,170,171,172,173,174,177,179,180,181,182,183,184,187,189,190,192,193,194,195,196,197,198,199,200,201,]),'TEXT':([7,20,36,41,70,101,],[41,61,76,79,100,125,]),'SYMBOL':([7,9,10,11,12,13,14,15,20,21,22,25,26,30,31,32,36,37,41,53,54,70,93,100,101,102,114,116,117,125,126,128,137,148,149,164,165,167,177,179,181,187,],[42,47,49,51,52,53,54,56,42,62,63,66,67,71,72,73,42,77,42,87,88,42,118,124,42,126,136,138,139,144,145,147,155,162,163,175,176,178,185,186,188,191,]),'POINTLIST':([86,],[110,]),}

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
  ('command -> SHAPE SYMBOL PLANE POINTLIST','command',4,'p_command_shape','mdl.py',242),
  ('command -> EXTRUSION SYMBOL SYMBOL NUMBER','command',4,'p_command_extrusion','mdl.py',248),
  ('command -> REVOLUTION SYMBOL SYMBOL XYZ NUMBER','command',5,'p_command_revolution','mdl.py',253),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',258),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',259),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',260),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',261),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',262),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',263),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',264),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',265),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',286),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',287),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',295),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',296),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',304),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',305),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',313),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',318),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',323),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',329),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',330),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',341),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',347),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',348),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',354),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',360),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',366),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',371),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',375),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',376),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',377),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',378),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',392),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',398),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',405),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',410),
  ('command -> WEB','command',1,'p_web','mdl.py',414),
  ('command -> PRINT TEXT','command',2,'p_print','mdl.py',418),
  ('command -> PRINT','command',1,'p_print','mdl.py',419),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',426),
]
