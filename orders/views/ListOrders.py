from django.http import HttpResponse
from django.shortcuts import render


def pedidos_lista(request):
    pedidos_lista = [
            {'pedido' : '002/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '003/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '007/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '008/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '009/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '010/17' , 'proveedor' : 'PERNOD'},
            {'pedido' : '010/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '011/18' , 'proveedor' : 'CYT'},
            {'pedido' : '015/18' , 'proveedor' : 'CYT'},
            {'pedido' : '018/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '020/18' , 'proveedor' : 'TRIVENTO'},
            {'pedido' : '022/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '024/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '025/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '026/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '027/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '028/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '029/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '029/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '032/18' , 'proveedor' : 'ACHAVAL'},
            {'pedido' : '033/18' , 'proveedor' : 'CYT'},
            {'pedido' : '035/18' , 'proveedor' : 'CYT'},
            {'pedido' : '037/18' , 'proveedor' : 'CYT'},
            {'pedido' : '038/18' , 'proveedor' : 'CYT'},
            {'pedido' : '039/18' , 'proveedor' : 'CYT'},
            {'pedido' : '040/17' , 'proveedor' : 'CYT'},
            {'pedido' : '040/18' , 'proveedor' : 'CYT'},
            {'pedido' : '042/18' , 'proveedor' : 'CYT'},
            {'pedido' : '044/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '045/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '046/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '046/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '047/17' , 'proveedor' : 'CYT'},
            {'pedido' : '047/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '047/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '048/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '049/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '050/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '051/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '052/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '053/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '053/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '054/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '060/18' , 'proveedor' : 'CYT'},
            {'pedido' : '063/18' , 'proveedor' : 'CYT'},
            {'pedido' : '065/18' , 'proveedor' : 'CYT'},
            {'pedido' : '070/18' , 'proveedor' : 'MUGA'},
            {'pedido' : '071/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '071/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '071/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '072/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '074/17' , 'proveedor' : 'SOGEVINUS'},
            {'pedido' : '074/17' , 'proveedor' : 'SOGEVINUS'},
            {'pedido' : '074/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '075/17' , 'proveedor' : 'LA RURAL'},
            {'pedido' : '075/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '075/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '076/18' , 'proveedor' : 'CYT'},
            {'pedido' : '077/18' , 'proveedor' : 'CYT'},
            {'pedido' : '078/17' , 'proveedor' : 'CYT'},
            {'pedido' : '079/18' , 'proveedor' : 'CYT'},
            {'pedido' : '082/18' , 'proveedor' : 'CYT'},
            {'pedido' : '084/18' , 'proveedor' : 'CYT'},
            {'pedido' : '085/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '086/17' , 'proveedor' : 'MAIPO'},
            {'pedido' : '086/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '087/17' , 'proveedor' : 'MAIPO'},
            {'pedido' : '087/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '090/17' , 'proveedor' : 'PRATAC'},
            {'pedido' : '092/17' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '094/17' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '095/17' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '097/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '101/17' , 'proveedor' : 'PRATAC'},
            {'pedido' : '104/18' , 'proveedor' : 'CYT'},
            {'pedido' : '105/18' , 'proveedor' : 'CYT'},
            {'pedido' : '106/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '107/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '109/18' , 'proveedor' : 'CYT'},
            {'pedido' : '111/17' , 'proveedor' : 'HENKELL'},
            {'pedido' : '111/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '111/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '111/18' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '112/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '118/18' , 'proveedor' : 'CYT'},
            {'pedido' : '119/18' , 'proveedor' : 'CYT'},
            {'pedido' : '120/18' , 'proveedor' : 'CYT'},
            {'pedido' : '123/18' , 'proveedor' : 'CYT'},
            {'pedido' : '124/18' , 'proveedor' : 'CYT'},
            {'pedido' : '125/18' , 'proveedor' : 'CYT'},
            {'pedido' : '126/18' , 'proveedor' : 'CYT'},
            {'pedido' : '127/18' , 'proveedor' : 'CYT'},
            {'pedido' : '128/18' , 'proveedor' : 'CYT'},
            {'pedido' : '129/18' , 'proveedor' : 'CYT'},
            {'pedido' : '130/18' , 'proveedor' : 'CYT'},
            {'pedido' : '131/18' , 'proveedor' : 'CYT'},
            {'pedido' : '132/18' , 'proveedor' : 'CYT'},
            {'pedido' : '134/18' , 'proveedor' : 'CYT'},
            {'pedido' : '135/18' , 'proveedor' : 'CYT'},
            {'pedido' : '136/18' , 'proveedor' : 'CYT'},
            {'pedido' : '137/18' , 'proveedor' : 'CYT'},
            {'pedido' : '138/18' , 'proveedor' : 'CYT'},
            {'pedido' : '139/18' , 'proveedor' : 'CYT'},
            {'pedido' : '140/18' , 'proveedor' : 'CYT'},
            {'pedido' : '141/18' , 'proveedor' : 'CYT'},
            {'pedido' : '142/18' , 'proveedor' : 'CYT'},
            {'pedido' : '143/18' , 'proveedor' : 'CYT'},
            {'pedido' : '144/18' , 'proveedor' : 'CYT'},
            {'pedido' : '145/18' , 'proveedor' : 'CYT'},
            {'pedido' : '146/18' , 'proveedor' : 'CYT'},
            {'pedido' : '147/18' , 'proveedor' : 'CYT'},
            {'pedido' : '148/18' , 'proveedor' : 'CYT'},
            {'pedido' : '149/18' , 'proveedor' : 'CYT'},
            {'pedido' : '150/18' , 'proveedor' : 'CYT'},
            {'pedido' : '151/18' , 'proveedor' : 'TRIVENTO'},
            {'pedido' : '152/17' , 'proveedor' : 'CYT'},
            {'pedido' : '152/18' , 'proveedor' : 'CYT'},
            {'pedido' : '153/17' , 'proveedor' : 'CYT'},
            {'pedido' : '153/18' , 'proveedor' : 'CYT'},
            {'pedido' : '154/18' , 'proveedor' : 'CYT'},
            {'pedido' : '155/18' , 'proveedor' : 'CYT'},
            {'pedido' : '156/18' , 'proveedor' : 'CYT'},
            {'pedido' : '157/17' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '157/18' , 'proveedor' : 'CONCHA Y TORO'},
            {'pedido' : '158/18' , 'proveedor' : 'CYT'},
            {'pedido' : '159/18' , 'proveedor' : 'CYT'},
            {'pedido' : '160/18' , 'proveedor' : 'CYT'},
            {'pedido' : '161/17' , 'proveedor' : 'CYT'},
            {'pedido' : '161/18' , 'proveedor' : 'CYT'},
            {'pedido' : '162/18' , 'proveedor' : 'CYT'},
            {'pedido' : '163/18' , 'proveedor' : 'CYT'},
            {'pedido' : '164/18' , 'proveedor' : 'CYT'},
            {'pedido' : '165/18' , 'proveedor' : 'CYT'},
            {'pedido' : '166/17' , 'proveedor' : 'HENKELL'},
            {'pedido' : '166/18' , 'proveedor' : 'CYT'},
            {'pedido' : '167/17' , 'proveedor' : 'GONZALEZ'},
            {'pedido' : '167/18' , 'proveedor' : 'CYT'},
            {'pedido' : '168/18' , 'proveedor' : 'CYT'},
            {'pedido' : '169/18' , 'proveedor' : 'CYT'},
            {'pedido' : '170/18' , 'proveedor' : 'CYT'},
            {'pedido' : '171/18' , 'proveedor' : 'CYT'},
            {'pedido' : '172/18' , 'proveedor' : 'CYT'},
            {'pedido' : '173/18' , 'proveedor' : 'CYT'},
            {'pedido' : '174/17' , 'proveedor' : 'CYT'},
            {'pedido' : '174/18' , 'proveedor' : 'CYT'},
            {'pedido' : '175/18' , 'proveedor' : 'CYT'},
            {'pedido' : '176/18' , 'proveedor' : 'CYT'},
            {'pedido' : '177/18' , 'proveedor' : 'CYT'},
            {'pedido' : '178/18' , 'proveedor' : 'CYT'},
            {'pedido' : '179/18' , 'proveedor' : 'CYT'},
            {'pedido' : '180/18' , 'proveedor' : 'CYT'},
            {'pedido' : '181/18' , 'proveedor' : 'CYT'},
            {'pedido' : '182/18' , 'proveedor' : 'CYT'},
            {'pedido' : '183/18' , 'proveedor' : 'CYT'},
            {'pedido' : '184/18' , 'proveedor' : 'CYT'},
            {'pedido' : '185/18' , 'proveedor' : 'CYT'},
            {'pedido' : '186/18' , 'proveedor' : 'CYT'},
            {'pedido' : '187/18' , 'proveedor' : 'CYT'},
            {'pedido' : '188/17' , 'proveedor' : 'CYT'},
            {'pedido' : '188/17' , 'proveedor' : 'CYT'},
            {'pedido' : '188/18' , 'proveedor' : 'CYT'},
            {'pedido' : '189/18' , 'proveedor' : 'CYT'},
            {'pedido' : '190/17' , 'proveedor' : 'CYT'},
            {'pedido' : '190/18' , 'proveedor' : 'CYT'},
            {'pedido' : '191/17' , 'proveedor' : 'CYT'},
            {'pedido' : '191/18' , 'proveedor' : 'CYT'},
            {'pedido' : '192/18' , 'proveedor' : 'CYT'},
            {'pedido' : '193/17' , 'proveedor' : 'MAIPO'},
            {'pedido' : '193/18' , 'proveedor' : 'CYT'},
            {'pedido' : '194/18' , 'proveedor' : 'CYT'},
            {'pedido' : '195/18' , 'proveedor' : 'CYT'},
            {'pedido' : '196/18' , 'proveedor' : 'CYT'},
            {'pedido' : '197/17' , 'proveedor' : 'MAIPO'},
            {'pedido' : '197/18' , 'proveedor' : 'CYT'},
            {'pedido' : '198/18' , 'proveedor' : 'CYT'},
            {'pedido' : '199/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '200/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '201/17' , 'proveedor' : 'PRATAC'},
            {'pedido' : '201/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '202/17' , 'proveedor' : 'HENKELL'},
            {'pedido' : '202/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '203/17' , 'proveedor' : 'CYT'},
            {'pedido' : '203/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '204/17' , 'proveedor' : 'CYT'},
            {'pedido' : '204/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '205/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '206/17' , 'proveedor' : 'CYT'},
            {'pedido' : '206/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '207/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '208/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '209/17' , 'proveedor' : 'PRATAC'},
            {'pedido' : '209/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '210/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '211/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '212/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '213/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '214/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '215/18' , 'proveedor' : 'CYT'},
            {'pedido' : '216/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '216/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '217/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '218/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '220/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '221/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '222/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '223/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '225/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '226/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '228/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '231/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '232/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '233/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '235/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '236/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '237/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '238/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '239/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '240/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '241/18' , 'proveedor' : 'TRIVENTO'},
            {'pedido' : '242/18' , 'proveedor' : 'TRIVENTO'},
            {'pedido' : '243/18' , 'proveedor' : 'TRIVENTO'},
            {'pedido' : '244/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '245/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '246/18' , 'proveedor' : 'HENKELL'},
            {'pedido' : '248/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '248/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '249/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '249/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '250/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '250/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '250/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '251/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '251/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '253/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '253/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '254/18' , 'proveedor' : 'LA RURAL'},
            {'pedido' : '255/18' , 'proveedor' : 'LA RURAL'},
            {'pedido' : '256/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '256/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '257/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '258/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '259/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '259/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '260/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '261/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '262/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '263/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '264/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '265/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '266/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '267/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '268/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '269/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '270/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '271/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '272/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '272/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '273/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '273/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '274/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '275/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '275/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '276/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '276/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '278/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '279/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '280/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '280/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '281/18' , 'proveedor' : 'CYT'},
            {'pedido' : '282/18' , 'proveedor' : 'CYT'},
            {'pedido' : '283/18' , 'proveedor' : 'CYT'},
            {'pedido' : '284/18' , 'proveedor' : 'CYT'},
            {'pedido' : '285/18' , 'proveedor' : 'CYT'},
            {'pedido' : '286/18' , 'proveedor' : 'CYT'},
            {'pedido' : '287/18' , 'proveedor' : 'CYT'},
            {'pedido' : '288/18' , 'proveedor' : 'CYT'},
            {'pedido' : '289/18' , 'proveedor' : 'CYT'},
            {'pedido' : '290/18' , 'proveedor' : 'CYT'},
            {'pedido' : '291/18' , 'proveedor' : 'CYT'},
            {'pedido' : '293/18' , 'proveedor' : 'CYT'},
            {'pedido' : '294/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '295/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '296/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '297/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '297/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '298/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '299/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '300/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '301/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '302/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '303/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '304/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '305/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '306/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '307/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '308/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '309/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '310/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '311/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '312/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '313/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '313/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '314/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '314/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '315/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '316/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '316/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '317/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '317/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '318/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '318/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '319/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '320/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '321/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '322/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '322/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '323/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '324/18' , 'proveedor' : 'MAIPO'},
            {'pedido' : '325/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '325/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '326/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '326/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '327/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '327/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '328/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '328/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '329/18' , 'proveedor' : 'CYT'},
            {'pedido' : '330/18' , 'proveedor' : 'CYT'},
            {'pedido' : '331/18' , 'proveedor' : 'CYT'},
            {'pedido' : '332/18' , 'proveedor' : 'CYT'},
            {'pedido' : '333/18' , 'proveedor' : 'CYT'},
            {'pedido' : '334/18' , 'proveedor' : 'CYT'},
            {'pedido' : '335/18' , 'proveedor' : 'GONZALEZ BYAS'},
            {'pedido' : '336/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '336/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '337/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '337/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '338/18' , 'proveedor' : 'PRATAC'},
            {'pedido' : '338/18' , 'proveedor' : 'PRATAC'},
    ]


    analisis = [
    '002/18',
    '003/18',
    '009/18',
    '010/17' ,
    '010/18',
    '011/18',
    '015/18',
    '018/18',
    '020/18',
    '022/18',
    '024/18',
    '026/18',
    '028/18',
    '029/18',
    '032/18',
    '035/18',
    '037/18',
    '038/18',
    '039/18',
    '040/17',
    '040/18',
    '042/18',
    '044/18',
    '045/18',
    '046/18',
    '047/17',
    '047/18',
    '048/18',
    '049/18',
    '050/18',
    '051/18',
    '052/18',
    '053/18',
    '054/18',
    '060/18',
    '063/18',
    '065/18',
    '070/18',
    '071/18',
    '072/18',
    '074/17',
    '074/18',
    '075/18',
    '076/18',
    '077/18',
    '082/18',
    '084/18',
    '086/18',
    '087/18',
    '090/17',
    '092/17',
    '101/17',
    '105/18',
    '106/18',
    '107/18',
    '109/18',
    '111/17',
    '111/18',
    '112/18',
    '118/18',
    '119/18',
    '120/18',
    '123/18',
    '124/18',
    '125/18',
    '126/18',
    '127/18',
    '128/18',
    '129/18',
    '130/18',
    '131/18',
    '132/18',
    '134/18',
    '135/18',
    '136/18',
    '137/18',
    '138/18',
    '139/18',
    '140/18',
    '141/18',
    '142/18',
    '143/18',
    '144/18',
    '145/18',
    '146/18',
    '147/18',
    '148/18',
    '149/18',
    '150/18',
    '151/18',
    '152/17',
    '152/18',
    '153/17',
    '153/18',
    '154/18',
    '155/18',
    '156/18',
    '157/17',
    '157/18',
    '158/18',
    '159/18',
    '160/18',
    '161/17',
    '161/18',
    '162/18',
    '163/18',
    '164/18',
    '165/18',
    '166/17',
    '166/18',
    '167/17',
    '167/18',
    '168/18',
    '169/18',
    '170/18',
    '171/18',
    '172/18',
    '173/18',
    '174/18',
    '175/18',
    '176/18',
    '177/18',
    '177/18',
    '178/18',
    '179/18',
    '180/18',
    '181/18',
    '182/18',
    '183/18',
    '184/18',
    '185/18',
    '186/18',
    '187/18',
    '188/17',
    '188/18',
    '189/18',
    '190/17',
    '190/18',
    '191/18',
    '192/18',
    '193/18',
    '194/18',
    '195/18',
    '196/18',
    '197/17',
    '197/18',
    '198/18',
    '199/18',
    '201/18',
    '202/18',
    '203/18',
    '204/18',
    '205/18',
    '206/18',
    '207/18',
    '208/18',
    '209/18',
    '210/18',
    '211/18',
    '212/18',
    '213/18',
    '214/18',
    '215/18',
    '216/18',
    '217/18',
    '218/18',
    '220/18',
    '221/18',
    '222/18',
    '223/18',
    '225/18',
    '226/18',
    '228/18',
    '231/18',
    '232/18',
    '235/18',
    '236/18',
    '237/18',
    '239/18',
    '240/18',
    '241/18',
    '242/18',
    '243/18',
    '244/18',
    '245/18',
    '246/18',
    '248/18',
    '249/18',
    '250/18',
    '251/18',
    '253/18',
    '254/18',
    '255/18',
    '256/18',
    '257/18',
    '258/18',
    '259/18',
    '260/18',
    '261/18',
    '262/18',
    '263/18',
    '264/18',
    '265/18',
    '266/18',
    '267/18',
    '268/18',
    '269/18',
    '270/18',
    '271/18',
    '272/18',
    '273/18',
    '274/18',
    '275/18',
    '276/18',
    '278/18',
    '279/18',
    '280/18',
    '281/18',
    '282/18',
    '283/18',
    '284/18',
    '285/18',
    '286/18',
    '287/18',
    '288/18',
    '289/18',
    '290/18',
    '291/18',
    '293/18',
    '294/18',
    '295/18',
    '296/18',
    '297/18',
    '298/18',
    '299/18',
    '300/18',
    '301/18',
    '302/18',
    '303/18',
    '304/18',
    '305/18',
    '306/18',
    '307/18',
    '308/18',
    '309/18',
    '310/18',
    '311/18',
    '312/18',
    '313/18',
    '314/18',
    '315/18',
    '316/18',
    '317/18',
    '318/18',
    '319/18',
    '320/18',
    '321/18',
    '322/18',
    '323/18',
    '324/18',
    '325/18',
    '326/18',
    '327/18',
    '328/18',
    '329/18',
    '330/18',
    '331/18',
    '332/18',
    '333/18',
    '334/18',
    '335/18',
    '336/18',
    '337/18',
    '338/18',
    ]

    coincidencias  = []

    for item in analisis:
        for x in list({v['pedido']:v for v in pedidos_lista}.values()):
            if item == x['pedido']:
                coincidencias.append(x)
                break   


    return render(request, 'lista_pedidos.html', {'orders': coincidencias})