import json
from django.test import TestCase
from labels.lib_src import (ActivateRangeSafeTrack, LoginSafeTrack)
from labels.models import Label
from logs.app_log import loggin


class TESTActivateRange(TestCase):

    def setUp(self) -> None:
        #self.for_activate = [
            ### ['CORDOVEZ','043-22','3031-53-024579-013-000750-66-108-000037','002FPBO7','002FQU64'],
            ### ['CORDOVEZ','005-22','3031-018-002474-013-001000-66-213-000077','002C65B0','002BYJQF','002D3K01','002CVZ31','002EMOV4','002E3R87','002EOBR0','002EV451'],
            ### ['CORDOVEZ','004-22','3031-018-002474-013-001000-66-213-000077','002F8S65','002F16L3','002D0E88','002F16L3'],
            ### ['CORDOVEZ','008-22','3031-018-002474-013-001000-66-213-000077','002E46H4','002E26M2','002E2ZZ0','002EY045','002EQ2J1','002E16Y5','002E66F0','002EP307'],
            ### ['CORDOVEZ','217-21','3031-053-001246-013-000750-66-108-000041','001EQ0M5','001FDH46'],
            ### ['CORDOVEZ','256-21','3031-053-001982-013-000750-66-101-000037','001FA7C0','001F2LR3'],
            ### ['CORDOVEZ','272-21','3031-053-036356-013-000750-66-209-000033','001G5SA0','001FTO81'],
            ### ['CORDOVEZ','290-21','3031-053-000402-013-000750-66-108-000037','002FBT68','002FOKF2'],
            ### ['CORDOVEZ','012-22','3031-018-000113-013-000750-66-213-000077','001TE4N0','001T6J26','001FZ9V9','001FROA5','001RUT80','001RN7N8','001R5QP8','001QY542','001BC6C3','001C76H8','002ELPL3','002EYKE2'],
            ### ['CORDOVEZ','025-22','3031-018-000466-013-000750-66-213-000077','001T5RT9','001SY683','001SBIW0','001S3XB7','001EWO42','001EP2J0','002CI0J5','002C8WI6','002FN1X5','002FEPT0','002EXT58','002ELOX4'],
            ### ['CORDOVEZ','077-22','3031-053-000491-031-001000-66-108-000026','001FSWZ4','001FM2N0','001GVIQ3','001GOOE4'],
            ### ['CORDOVEZ','079-22','3031-053-000491-031-001000-66-108-000026','002E4ZX6','002DWN36'],
            ### ['CORDOVEZ','078-22','3031-053-000491-031-001000-66-108-000026','001DRU30','001E36G5'],
            ### ['CORDOVEZ','078-22','3031-053-000491-031-001000-66-108-000026','0019LOK6','0019E2Z4','001CCS43','001C56J1','002EDCR7','002E5R63','002D2E64','002CU1C1','002BZSF9','002BRFL2','002FFYI1','002F8CX0','002DAR00','002D35F9','002F7LO5','002EZ8U2','001BIJ83','001CDJD8','001AOAB5','001AGOQ9'],
            ### ['CORDOVEZ','039-22','3031-053-024580-013-000750-66-108-000037','001HC8E7','001H4WTO'],
            ### ['IMNAC','002-22','3031-053-025611-013-000750-66-211-000026','001SHFB5','001SOZK9'],
            ### ['IMNAC','002-22','3031-053-026905-013-000750-66-211-000027','0019MI05','0019FNO3'],
            ### ['IMNAC','003-22','3031-053-026345-013-000750-66-211-000033','001AP3R1','001AI9F2','001TC3CM0','001TC3CM0'],
            ### ['IMNAC','003-22','3031-053-025610-013-000750-66-211-000021','001RPOT3','001S6CI0'],
            ### ['IMNAC','003-22','3031-053-026904-013-000750-66-211-000026','001SFGL1','001RGN44'],
            ### ['IMNAC','016-22','3031-056-023963-013-000750-66-209-000021','001AFXH4','001BAXM9','001BMC29','001BJAH8'],
            ### ['IMNAC','095-21','3031-053-023965-013-000750-66-209-000027','001AVGN1','001ANV28','0019NOI2','0019G2X0','0019KI29','0019CWH2','001D0O51','001CT2K3','001AEQZ4','001B9R41','0019SUW2','0019L9B3','0019C582','001A75D7','001BJOM0','001BQGT4'],
            ### ['IMNAC','105-21','3031-056-023964-013-000750-66-209-000021','001B5W06','001B4AF4','001AL3V9','001DIA5'],
            ### ['IMNAC','004-22','3031-053-026343-013-000750-66-211-000029','0019WTY7','001A3M25'],
            ### ['IMNAC','004-22','3031-053-025606-013-000750-66-211-000033','001CHYI1','001DCYO6'],
            ### ['IMNAC','004-22','3031-053-026905-013-000750-66-211-000027','001CB6U0','001BOGV8'],
            ### ['IMNAC','004-22','3031-053-026345-013-000750-66-211-000033','001BW264','001C4DX0'],
            ### ['IMNAC','004-22','3031-053-025610-013-000750-66-211-000021','001AZVQ0','001A55F0'],
            ### ['IMNAC','004-22','3031-053-026344-013-000187-66-211-000033','002EGI73','002E8XM7','002FRH56','002FCC56','0019EO57','001RAWI6'],
            ### ['VID','022-21','3031-53-027056-013-000750-66-108-000041','001TL0LF9','001SSZU6','001SZ1M8','001SS8L6'],
            ### ['VID','022-21','3031-53-027056-013-000750-66-108-000041','002A6MW4','0029Z1B9','00294152','0028WFK0','002AEZQ0','002A7E51','001RHA03','001SCA58'],
            ### ['VID','022-21','3031-53-027056-013-000750-66-108-000041','00289S80','002826N8','001RRMS3','001RK174','001U8DK8','001U0RZ1','001QJUN4','001QC925'],
            ### ['VID','022-21','3031-53-027056-013-000750-66-108-000041','001SACE3','001S2QT7','001QLUL0','001QE901','001S3627','001RVKH4','001S8CG7','001S0QV0'],
            ### ['VID','024-21','3031-53-036360-013-000750-66-209-000146','001CXHP9','001CPW45'],
            ### ['VID','024-21','3031-53-036359-013-000750-66-209-000146','001A6E42','0019YSI0']
        #]
        return super().setUp()

    def test_activate_range(self):
        ranges = [
            '001D22I0',
            '001D2TR0',
        ]
        loggin('t', 'intentando activar rango')
        login = LoginSafeTrack()
        activateRange = ActivateRangeSafeTrack(login)
        label = Label.objects.get(pk=19)
        label.initial_range = ranges[0]
        label.end_range = ranges[1]
        label.quantity = 2
        result_label = activateRange.try_activate(
            label, ignore_diferences=True
        )
        recovery = Label.objects.get(pk=19)
        self.assertEqual(recovery, result_label)
    
    def activate_range_fail(self):
        '''Make test with labels actived'''
        ranges = [
            '001D3L08',
            '001D4C92',
        ]
        loggin('t', 'intentando activar rango')
        login = LoginSafeTrack()
        activateRange = ActivateRangeSafeTrack(login)
        label = Label.objects.get(pk=19)
        label.initial_range = ranges[0]
        label.end_range = ranges[1]
        label.quantity = 2
        result_label = activateRange.try_activate(label, ignore_diferences=True)
        response  = json.loads(result_label.response)
        self.assertEqual('httpCode', response['httpCode'])
