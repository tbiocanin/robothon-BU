import re
import math

class Coords():

    def __init__(self,s):
        self.joints, self.position, self.orientation, self.rpy, self.pos_board_cs = self.extract_data(s)

   
    def extract_data(self,s):
        # Extract joints
        joints = re.findall(r'-?\d+\.\d+', s.split('\n')[0])
        
        # Extract position
        position = []
        position_regex = r'position:\s*\n\s*x:\s*(-?\d+\.\d+)\s*\n\s*y:\s*(-?\d+\.\d+)\s*\n\s*z:\s*(-?\d+\.\d+)'
        position_match = re.search(position_regex, s)
        if position_match:
            position = [float(position_match.group(1)), float(position_match.group(2)), float(position_match.group(3))]
        
        # Extract orientation
        orientation = []
        orientation_regex = r'orientation:\s*\n\s*x:\s*(-?\d+\.\d+)\s*\n\s*y:\s*(-?\d+\.\d+)\s*\n\s*z:\s*(-?\d+\.\d+)\s*\n\s*w:\s*(-?\d+\.\d+)'
        orientation_match = re.search(orientation_regex, s)
        if orientation_match:
            orientation = [float(orientation_match.group(1)), float(orientation_match.group(2)), float(orientation_match.group(3)), float(orientation_match.group(4))]
        
        # Extract rpy
        rpy = []
        rpy_regex = r'RPY = \[(.*?)\]'
        rpy_match = re.search(rpy_regex, s)
        if rpy_match:
            rpy_str = rpy_match.group(1).strip()
            rpy = [float(x.strip()) for x in rpy_str.split(',')]

        joints = [float(joint) for joint in joints]
        pos_board_cs = [position[0] - 0.479786920544, position[1] - 0.00132797830077, position[2] - 0.086379691919]
        return joints, position, orientation, rpy, pos_board_cs

# define a function to transform coordinates
def transform_coordinates(local_coords, board_origin, board_angle):

    # calculate the new coordinates in the robot's coordinate system
    robot_x = math.cos(board_angle) * local_coords[0] + math.sin(board_angle) * local_coords[1] + board_origin[0]
    robot_y = -math.sin(board_angle) * local_coords[0] + math.cos(board_angle) * local_coords[1] + board_origin[1]

    return [robot_x, robot_y]

# define the local task board coordinates and board origin

board_origin = [1,1]
board_angle = math.pi / 4 




start_button_approach = Coords('''joints = [0.271870232572 0.159104162302 -0.0736630360735 -2.39942199593 0.0135551755486 2.594682936 0.966274300607]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681995541
    nsecs: 817485094
  frame_id: "/world"
pose: 
  position: 
    x: 0.493943242496
    y: 0.0984648762057
    z: 0.253280172136
  orientation: 
    x: -0.925061326361
    y: 0.379369154086
    z: -0.0165099124738
    w: 0.00824682912067 ]
panda_link8 RPY = [-3.1138000993448074, -0.024285958224517384, -0.7787179084494085]''')

local_coords = [2,1]
# transform the coordinates to the robot's coordinate system
robot_coords = transform_coordinates(local_coords, board_origin, board_angle)

# print out the results
print("Globalne koordinate:" + str(robot_coords))


start_button_press = Coords('''joints = [0.276703244013 0.275328226354 -0.0700943851063 -2.34716334547 0.035250341843 2.60833572999 0.993683239015]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681997180
    nsecs: 650679111
  frame_id: "/world"
pose: 
  position: 
    x: 0.503394660416
    y: 0.103808170816
    z: 0.214307044193
  orientation: 
    x: 0.918083953716
    y: -0.396330303242
    z: -0.00507502715353
    w: 0.00428821179053 ]
panda_link8 RPY = [3.1296862940369747, 0.005924702346895347, -0.8150890470720284]''')

start_button_depart = Coords('''joints = [0.276717146995 0.203739311009 -0.076398581921 -2.34849551667 0.0352137333109 2.55607748323 0.989105987273]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681997278
    nsecs: 417503118
  frame_id: "/world"
pose: 
  position: 
    x: 0.505106577216
    y: 0.101508780203
    z: 0.246053729207
  orientation: 
    x: -0.917816821177
    y: 0.396992130571
    z: -0.000773307508641
    w: 0.0029888167333 ]
panda_link8 RPY = [-3.1354898277608774, 0.0009522010419122964, -0.8164546350056683]''')

slider_snapshot = Coords('''joints = [0.189035494974 0.354442183739 -0.101295066353 -2.18477988313 0.0351273777994 2.53071234676 -0.709063934159]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681997632
    nsecs: 904539108
  frame_id: "/world"
pose: 
  position: 
    x: 0.557780127671
    y: 0.0483745660159
    z: 0.224313306444
  orientation: 
    x: 0.925995583428
    y: 0.377446001647
    z: -0.00530244324258
    w: 0.00621123250164 ]
panda_link8 RPY = [3.134086757536471, 0.014505424460589835, 0.774041377274029]''')

slider_approach = Coords('''joints = [0.192749941181 0.478827290359 -0.0914787598043 -1.92670335761 0.0393318030967 2.40903549168 -0.694282036432]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681997806
    nsecs: 137871026
  frame_id: "/world"
pose: 
  position: 
    x: 0.622817422735
    y: 0.0660710884705
    z: 0.240704214899
  orientation: 
    x: 0.925495860062
    y: 0.378664963636
    z: 0.00053276232977
    w: 0.00836507540487 ]
panda_link8 RPY = [3.125714021364724, 0.0053593690741117715, 0.7766893228613874]''')

slider_push = Coords('''joints = [0.208819320562 0.524114647401 -0.0981062594283 -1.92132717429 0.0400320090088 2.40900986009 -0.687297970638]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681997985
    nsecs: 657588958
  frame_id: "/world"
pose: 
  position: 
    x: 0.619325191028
    y: 0.0714759196786
    z: 0.214844583332
  orientation: 
    x: 0.924709309765
    y: 0.380132709025
    z: -0.0193019382588
    w: 0.00626507325405 ]
panda_link8 RPY = [-3.138509937810762, 0.040464522904350535, 0.7801138176377815]''')

slider_max_position = Coords('''joints = [0.234298684561 0.468080868554 -0.116906037282 -2.01048065959 0.0325354716817 2.40405584383 -0.685343891725]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1681998219
    nsecs:  44620990
  frame_id: "/world"
pose: 
  position: 
    x: 0.593443570774
    y: 0.0714276814109
    z: 0.21447022837
  orientation: 
    x: 0.922596390483
    y: 0.383802174839
    z: -0.0384968415066
    w: 0.00545747655989 ]
panda_link8 RPY = [-3.122066072152101, 0.07528651466666478, 0.7891599579473016]''')

test_port_take_out_approach = Coords('''joints = [0.265749519336 0.256804145181 -0.16912505799 -2.37014765241 0.00282145871888 2.60552522951 0.873920564855]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682006253
    nsecs: 619752883
  frame_id: "/world"
pose: 
  position: 
    x: 0.504854020562
    y: 0.0466532195967
    z: 0.317059977973
  orientation: 
    x: 0.925679281007
    y: -0.377638608123
    z: 0.00180497800513
    w: 0.0224430930026 ]
panda_link8 RPY = [3.1013888799747575, -0.020294433195789233, -0.7742742344255571]''')

test_port_take_out = Coords('''joints = [0.265749519336 0.256804145181 -0.16912505799 -2.37014765241 0.00282145871888 2.60552522951 0.873920564855]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682006253
    nsecs: 619752883
  frame_id: "/world"
pose: 
  position: 
    x: 0.504854020562
    y: 0.0466532195967
    z: 0.217059977973
  orientation: 
    x: 0.925679281007
    y: -0.377638608123
    z: 0.00180497800513
    w: 0.0224430930026 ]
panda_link8 RPY = [3.1013888799747575, -0.020294433195789233, -0.7742742344255571]''')

test_port_take_out_depart = Coords('''joints = [0.265749519336 0.256804145181 -0.16912505799 -2.37014765241 0.00282145871888 2.60552522951 0.873920564855]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682006253
    nsecs: 619752883
  frame_id: "/world"
pose: 
  position: 
    x: 0.504854020562
    y: 0.0466532195967
    z: 0.317059977973
  orientation: 
    x: 0.925679281007
    y: -0.377638608123
    z: 0.00180497800513
    w: 0.0224430930026 ]
panda_link8 RPY = [3.1013888799747575, -0.020294433195789233, -0.7742742344255571]''')

test_port_plug_in_prepare = Coords('''joints = [0.909175806677 0.218485665211 -0.784565117386 -2.4826473218 0.391177351199 2.65509583779 0.602036247797]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682353967
    nsecs: 674159049
  frame_id: "/world"
pose: 
  position: 
    x: 0.525049754698
    y: 0.0387101359142
    z: 0.23202802747
  orientation: 
    x: -0.919358581859
    y: 0.392491997072
    z: -0.0137940008917
    w: 0.0232283390882 ]
panda_link8 RPY = [-3.0880222160144855, -0.007123065203446392, -0.8071777542758173]''')

test_port_plug_in = Coords('''joints = [0.264208814265 0.304316648843 -0.169010053273 -2.29421158995 0.000142696448799 2.59029946937 0.91022988131]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682006388
    nsecs: 453110933
  frame_id: "/world"
pose: 
  position: 
    x: 0.527848611456
    y: 0.048641052733
    z: 0.21822850704
  orientation: 
    x: 0.919276196545
    y: -0.392801947488
    z: 0.01040096001
    w: 0.0230157456126 ]
panda_link8 RPY = [3.107415458977034, -0.037206408850144125, -0.8069751767341896]''')

test_port_plug_in_approach = Coords('''joints = [0.264208814265 0.304316648843 -0.169010053273 -2.29421158995 0.000142696448799 2.59029946937 0.91022988131]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682006388
    nsecs: 453110933
  frame_id: "/world"
pose: 
  position: 
    x: 0.527848611456
    y: 0.048641052733
    z: 0.31822850704
  orientation: 
    x: 0.919276196545
    y: -0.392801947488
    z: 0.01040096001
    w: 0.0230157456126 ]
panda_link8 RPY = [3.107415458977034, -0.037206408850144125, -0.8069751767341896]''')

hatch_approach = Coords('''joints = [0.514404692487 0.304153530904 -0.590411468665 -2.32450332528 0.373428094648 2.5221574481 1.00313951457]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682172737
    nsecs: 550496101
  frame_id: "/world"
pose: 
  position: 
    x: 0.513229098735
    y: -0.0494928284052
    z: 0.226860635986
  orientation: 
    x: -0.773846767021
    y: 0.632846511438
    z: 0.0230585742129
    w: 0.0116093190049 ]
panda_link8 RPY = [3.1303644692960133, 0.05040256159503262, -1.3712798459268292]''')

hatch_grasped = Coords('''joints = [-0.0994117724279 0.152152100966 0.00164046620578 -2.53366042404 -0.0021964133325 2.72177465401 1.28641403682]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682358369
    nsecs: 711666107
  frame_id: "/world"
pose: 
  position: 
    x: 0.512124806709
    y: -0.0452267316108
    z: 0.220591345957
  orientation: 
    x: -0.77041463513
    y: 0.637289480528
    z: -0.0150883946123
    w: 0.00978510778999 ]
panda_link8 RPY = [-3.107276963778292, -0.010778328092934926, -1.382404428130833]''')

hatch_grasped_turn = Coords('''joints = [-0.0984209628432 0.153450097814 0.00160886362701 -2.53567996195 -0.00301316570624 2.72171841132 0.697273489986]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682358538
    nsecs:  78157901
  frame_id: "/world"
pose: 
  position: 
    x: 0.511192457278
    y: -0.0446517657652
    z: 0.219314316164
  orientation: 
    x: -0.922610173631
    y: 0.385388855372
    z: -0.0157211658538
    w: 0.00432927379879 ]
panda_link8 RPY = [-3.121486801615278, -0.025667113930028754, -0.7916218546685341]''')

hatch_lift_15 = Coords('''joints = [-1.02824849914 0.331940517962 0.923503667585 -2.34819888911 -0.409933773538 2.32578601176 1.00116394698]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682359479
    nsecs: 754951000
  frame_id: "/world"
pose: 
  position: 
    x: 0.538104953749
    y: -0.0442696377173
    z: 0.230467739466
  orientation: 
    x: 0.918717831892
    y: -0.384576450886
    z: -0.0802147188256
    w: 0.0403000951786 ]
panda_link8 RPY = [3.0044884375605068, 0.11665648745796087, -0.8008858987643167]''')

hatch_lift_30 = Coords('''joints = [-2.17848094092 -0.568654917498 2.05634947971 -2.14072043783 0.468233941134 1.97468951995 0.326275141652]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682359624
    nsecs: 219425916
  frame_id: "/world"
pose: 
  position: 
    x: 0.568187487403
    y: -0.0416934716014
    z: 0.241721169456
  orientation: 
    x: 0.912882246756
    y: -0.363075249054
    z: -0.170571877138
    w: 0.0756809210493 ]
panda_link8 RPY = [2.8670445679814636, 0.2593670166679252, -0.7931082607655272]''')

hatch_lift_60 = Coords('''joints = [0.22454843783 0.548303953422 -0.321845412361 -1.74539878599 0.0533119847527 1.56588018551 0.623611084016]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682359902
    nsecs: 334816932
  frame_id: "/world"
pose: 
  position: 
    x: 0.623240018009
    y: -0.0395298143227
    z: 0.242758325214
  orientation: 
    x: 0.871556225003
    y: -0.34633427428
    z: -0.314326997562
    w: 0.14710831289 ]
panda_link8 RPY = [2.5832843957599705, 0.46230430556542895, -0.891184818000357]''')

hatch_lift_75 = Coords('''joints = [0.166312257951 0.904551645226 -0.308987975836 -1.22803827713 0.059747089137 1.05332245058 0.56679923241]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682360097
    nsecs: 686913013
  frame_id: "/world"
pose: 
  position: 
    x: 0.667802865885
    y: -0.037787920693
    z: 0.216913730056
  orientation: 
    x: 0.80513768615
    y: -0.310695601065
    z: -0.461939659415
    w: 0.204531906749 ]
panda_link8 RPY = [2.242009117354127, 0.664610755381332, -1.0667637950896]''')

hatch_lift_90 = Coords('''joints = [0.10120932679 1.19307167266 -0.327972543683 -0.763244731334 0.107668305424 0.744450977388 0.608449069849]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682360355
    nsecs: 859833002
  frame_id: "/world"
pose: 
  position: 
    x: 0.693921012413
    y: -0.041578454296
    z: 0.199763598286
  orientation: 
    x: 0.761127276343
    y: -0.325486637185
    z: -0.511454737402
    w: 0.230559688171 ]
panda_link8 RPY = [2.067273094325375, 0.6795927899636269, -1.2232404968464319]''')

hatch_lift_100 = Coords('''joints = [0.0828319909472 1.16772140769 -0.272067410088 -0.767496659956 0.0729176225 0.822418420122 0.624806338646]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682360631
    nsecs:  34301042
  frame_id: "/world"
pose: 
  position: 
    x: 0.705312243354
    y: -0.0391888383177
    z: 0.205859844378
  orientation: 
    x: 0.786869874155
    y: -0.326640240627
    z: -0.474874960765
    w: 0.220535090152 ]
panda_link8 RPY = [2.1729106393880486, 0.6475899119531744, -1.1364773547207219]''')

hatch_lift_depart = Coords('''joints = [0.0852277483252 1.12524233134 -0.272112721664 -0.764028405487 0.132838463344 1.2204793403 0.629042772642]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682361376
    nsecs: 638434886
  frame_id: "/world"
pose: 
  position: 
    x: 0.765201910637
    y: -0.0338143237805
    z: 0.224981874414
  orientation: 
    x: 0.882114157727
    y: -0.343658765416
    z: -0.289809400066
    w: 0.140654816217 ]
panda_link8 RPY = [2.627688462455109, 0.4275178170886068, -0.8569393132013787]
''')

cable_approach = Coords('''joints = [0.202170961477 0.0804114401685 -0.417244245114 -2.53881864177 0.0598394061723 2.71265395346 0.552742318503]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682361777
    nsecs: 603135108
  frame_id: "/world"
pose: 
  position: 
    x: 0.507122721786
    y: -0.104073465732
    z: 0.254700661029
  orientation: 
    x: -0.916315381728
    y: 0.397248464643
    z: -0.0502257987947
    w: 0.00609488990004 ]
panda_link8 RPY = [-3.0903052166568656, -0.08730818140015416, -0.8203943158329213]''')

cable_grab = Coords('''joints = [0.205985760651 0.221722487519 -0.386936056154 -2.46749116172 0.178037345919 2.69449847126 0.407230535628]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682362014
    nsecs: 636423110
  frame_id: "/world"
pose: 
  position: 
    x: 0.522230979495
    y: -0.0981094837308
    z: 0.215600781477
  orientation: 
    x: 0.932546169132
    y: -0.360778269636
    z: 0.0140164107017
    w: 0.000472045393677 ]
panda_link8 RPY = [-3.1323617412985914, -0.026478531223097353, -0.7383999786164427]''')

cable_take_out = Coords('''joints = [0.376391180591 0.181646340295 -0.568070313596 -2.53832296717 0.267053756192 2.68407967541 0.325337355801]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682362338
    nsecs: 543468952
  frame_id: "/world"
pose: 
  position: 
    x: 0.495864377087
    y: -0.103239477067
    z: 0.215885348498
  orientation: 
    x: -0.930543177389
    y: 0.366039181733
    z: -0.00122126940754
    w: 0.0101597712212 ]
panda_link8 RPY = [-3.121792338880775, 0.005162570631550802, -0.749488347608046]''')

cable_depart = Coords('''joints = [0.367523164797 -0.222238154093 -0.589983605878 -2.43371566088 -0.142400211442 2.2743727845 0.580763004811]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682362392
    nsecs: 943789005
  frame_id: "/world"
pose: 
  position: 
    x: 0.502455328449
    y: -0.10610279288
    z: 0.377209201093
  orientation: 
    x: -0.938738972639
    y: 0.344202004796
    z: -0.0143905315023
    w: 0.00932918783659 ]
panda_link8 RPY = [-3.1141569175243, -0.020591434238175686, -0.7031788123242041]''')

cable_plug_in_approach = Coords('''joints = [0.137779423699 -0.0248381777014 -0.645194367108 -2.60752658981 1.8073839389 1.68404919758 1.28873495439]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682438489
    nsecs: 304598093
  frame_id: "/world"
pose: 
  position: 
    x: 0.462834829114
    y: -0.121625957709
    z: 0.296028468241
  orientation: 
    x: -0.0163571470306
    y: 0.692335120748
    z: 0.50694226528
    w: 0.513238798214 ]
panda_link8 RPY = [1.5113060285340802, 0.8143100563977844, 2.33034848006302]''')

cable_plug_in_prepare = Coords('''joints = [0.254778935799 0.475399713416 -0.665380303383 -2.52044619269 2.12169861147 1.47938460007 1.19273422896]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682439208
    nsecs:  45439958
  frame_id: "/world"
pose: 
  position: 
    x: 0.481727490782
    y: -0.106216432565
    z: 0.157946370731
  orientation: 
    x: 0.0493503626402
    y: 0.718559499727
    z: 0.486753555545
    w: 0.494274987455 ]
panda_link8 RPY = [1.6209086812903049, 0.7238695798984425, 2.3131665091742675]''')

cable_plugged_in = Coords('''joints = [0.253399661344 0.502619115616 -0.659110402584 -2.51377550528 2.12200857108 1.47743412572 1.16592534402]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682439261
    nsecs: 145445108
  frame_id: "/world"
pose: 
  position: 
    x: 0.480186283994
    y: -0.105507962895
    z: 0.148444789853
  orientation: 
    x: 0.0408692269516
    y: 0.725334807565
    z: 0.479514785003
    w: 0.492224231612 ]
panda_link8 RPY = [1.6461671823306239, 0.7407698969397285, 2.3377474686073714]''')

cable_wrap_prepare = Coords('''joints = [0.557176181312 -0.234949388489 -0.522997144604 -0.965315436063 -0.170102409449 0.890951387617 0.651829693669]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682439744
    nsecs: 556123971
  frame_id: "/world"
pose: 
  position: 
    x: 0.325118654316
    y: -0.0743967191197
    z: 0.894290259079
  orientation: 
    x: -0.932624827528
    y: 0.355573283971
    z: -0.0591329280993
    w: 0.0167889135935 ]
panda_link8 RPY = [-3.067797531765308, -0.09851913882123099, -0.7321389100283087]''')

cable_wrap_prepare = Coords('''joints = [0.557176181312 -0.234949388489 -0.522997144604 -0.965315436063 -0.170102409449 0.890951387617 0.651829693669]
panda_link8 pose = [
header: 
  seq: 0
  stamp: 
    secs: 1682439744
    nsecs: 556123971
  frame_id: "/world"
pose: 
  position: 
    x: 0.325118654316
    y: -0.0743967191197
    z: 0.894290259079
  orientation: 
    x: -0.932624827528
    y: 0.355573283971
    z: -0.0591329280993
    w: 0.0167889135935 ]
panda_link8 RPY = [-3.067797531765308, -0.09851913882123099, -0.7321389100283087]''')


