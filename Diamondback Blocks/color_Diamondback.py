


'''
###################Structural elements#####################:
1x1_end_beam 10055    black 0,0,0

1x2_beam 25568 green 0, .8, 0

1x3_beam 40144 yellow .8, .8, 0

10nm_bar_pin 27,306 orange .8 .319 0

90_2h_bracket 34561 red 1,0,0

90_2h_flat_bracket 35715 pink .8 0 .4

box_bracket 34882  blue 0 0 .8

cross_bracket 60188 mint 0 .8 .167

gear_beam 20110 36rows  orange .8 .319 0

gear_bushing_clip 8151 gray .084 .084 .084

hex_c2h_pin 9919 white 1,1,1

hex_guide_clip 11307 gray .084 .084 .084

T-bracket 48734 aqua 0 .8 .688

2_axle_pin_beam 19128 violet .8 .0 .676

1x2_beam_with_male_coupler 33019  green 0, .8, 0

###################Mechanical elements#####################:

36_bearing_hex_frame 7410  gray .084 .084 .084

36_bearing_on_clip_90 14655 gray .084 .084 .08

36_bearing_on_clip_0 15946 gray .084 .084 .084

32T_gear_with_female_coupler 77460 white 1,1,1

16T_gear_hex 711882 white 1,1,1

hex_axle_20nm 15481 aqua

32T_turntable 91920  black 0 .0 0

double_coupler 8497 pink .8 0 .4

clutch_plates 14616 white 1,1,1

'''



def color_large_groups():
    black = SBColor(0.0, 0.0, 0.0)          # RGB
    green = SBColor(0.0, 0.8, 0.0)
    yellow = SBColor(0.8, 0.8, 0.0)
    orange = SBColor(0.8, 0.319, 0.0)
    red = SBColor(1.0, 0.0, 0.0)
    pink = SBColor(0.8, 0.0, 0.4)
    blue = SBColor(0.0, 0.0, 0.8)
    mint = SBColor(0.0, 0.8, 0.167)
    gray = SBColor(0.84, 0.84, 0.84)
    white = SBColor(1.0, 1.0, 1.0)
    aqua = SBColor(0.0, 0.8, 0.688)
    brick = SBColor(0.8, 0.8, 0.0) #this ia val of 85, not sure how to set that to make it darker
    violet = SBColor(0.8, 0.0, 0.676)
    

    
    groups = SAMSON.getNodes('node.type sg')
    with SAMSON.holding("Colorize large groups"):
        for g in groups:
            atoms = g.getNodes('node.type atom')
            if len(atoms) == 10055:
                color = black
            elif len(atoms) == 25568:
                color = green
            elif len(atoms) == 40144:
                color = yellow 
            elif len(atoms) == 27306:
                color = orange  
            elif len(atoms) == 34561:
                color = red
            elif len(atoms) == 35715:
                color = pink  
            elif len(atoms) == 34882:
                color = blue  
            elif len(atoms) == 60188:
                color = mint
            elif len(atoms) == 20110:
                color = orange
            elif len(atoms) == 8151:
                color = gray
            elif len(atoms) == 9919:
                color = white
            elif len(atoms) == 48734:
                color = aqua 
            elif len(atoms) == 44290:
                color = gray
            elif len(atoms) == 39835:
                color = orange
            elif len(atoms) == 19128:
                color = violet
            elif len(atoms) == 7410:
                color = gray
            elif len(atoms) == 77460:
                color = white
            elif len(atoms) == 33019:
                color = green 
            elif len(atoms) == 14655:
                color = gray
            elif len(atoms) == 15946:
                color = gray   
            elif len(atoms) == 11882:
                color = white
            elif len(atoms) == 15481:
                color = aqua
            elif len(atoms) ==91920:
                color = black 
            elif len(atoms) ==8497:
                color = pink
            elif len(atoms) ==14616:
                color = white             
                
            
            
            for a in atoms:
                if hasattr(a, 'setColor'): a.setColor(color)


color_large_groups()


#trying to combine the naming and coloring into one function has not worked because
#if always names the last sg in the model so using two functions

with SAMSON.holding("Rename SGs with 10055 atoms"):
    for sg in SAMSON.getNodes('node.type sg'):
        if sum(1 for _ in sg.getNodes('node.type atom')) == 10055:
            sg.name = '1x1_end_beam'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 25568:
            sg.name = '1x2_beam'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 40144:
            sg.name = '1x3_beam'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 27306:
            sg.name = '10nm_bar_pin' 
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 34561:
            sg.name = '90_2h_bracket' 
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 35715:
            sg.name = '90_2h_flat_bracket' 
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 34882:
            sg.name = 'box_bracket'     
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 60188:
            sg.name = 'cross_bracket'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 20110:
            sg.name = 'gear_beam'    
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 8151:
            sg.name = 'gear_bushing_clip'  
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 9919:
            sg.name = 'hex_c2h_pin'  
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 11307:
            sg.name = 'hex_guide_clip'         
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 48734:
            sg.name = 'T-bracket'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 44290:
            sg.name = 'hex tile'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 39835:
            sg.name = 'square_edge_4hex_tile'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 19128:
            sg.name = '2_axle_pin_beam'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 7410:
            sg.name = '36_bearing_hex_frame'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 77460:
            sg.name = '32T_gear_with_female_coupler'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 33019:
            sg.name = '1x2_beam_with_male_coupler'         
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 14655:
            sg.name = '36_bearing_on_clip_90'   
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 15946:
            sg.name = '36_bearing_on_clip_0'  
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 11882:
            sg.name = '16_gear_hex'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 15481:
            sg.name = 'hex_axle_20nm'  
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 91920:
            sg.name = '32T_turntable'
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 8497:
            sg.name = 'double_coupler' 
        elif sum(1 for _ in sg.getNodes('node.type atom')) == 14616:
            sg.name = 'clutch_plates'         
            
            

            
    
            
          
            
            
            