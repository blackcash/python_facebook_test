#�ϥ�pythonŪ��facebook�峹�������g��,�ñN�q����X���d���M���g���H

1.���otoken�M�n����X�Ӫ��峹<br>
(1)�s�Wfacebook�}�o�̥��x(https://developers.facebook.com/tools-and-support/)<br>
(2)���"�ϧ� API ���դu��",�Y�i���otoken <br>
(3)�b�R�O�C��"me/posts"�Y�i��X�ۤv��po���峹,�b�q����X�峹��id <br>
<br>
2.�w��facebook sdk: <br>
       pip install facebook-sdk<br>
<br>
3.�{��:<br>
(1)�פJ�n�ϥΪ�facebook api : import facebook  <br>
(2)�غc�ϥΪ�����:graph = facebook.GraphAPI(access_token=token,version=version) <br>
(3)�ϥΪ�����o���(���o���d���B����1000��):graph.get_object(id=object_id+'?fields=comments.limit(1000)') <br>
