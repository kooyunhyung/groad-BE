from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.db import connection
from .models import user, alarm, qrcode, review, pedometer
import json
from .serializer import UserSerializer, PedometerSerializer, ReviewSerializer, AlarmSerializer, QrcodeSerializer, \
    LoginSerializer


# user의 목록을 보여주는 역할
class Groad_user_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_user")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        error_code = {
            'code': -3
        }
        sucess_code = {
            'code': 200
        }

        data = json.loads(request.body)
        gu_id = data.get('gu_id')
        gu_pw = data.get('gu_pw')
        gu_name = data.get('gu_name')
        gu_gender = data.get('gu_gender')
        gu_birth_date = data.get('gu_birth_date')
        gu_email = data.get('gu_email')
        gu_phone_number = data.get('gu_phone_number')

        sql = f"""INSERT INTO groad_user
        (gu_id, gu_pw, gu_name, gu_gender, gu_birth_date, gu_email, gu_phone_number)
            value('{gu_id}','{gu_pw}','{gu_name}','{gu_gender}','{gu_birth_date}','{gu_email}','{gu_phone_number}')
        """
        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(sucess_code)


# user의 login 기능 작성
class Groad_user_login(APIView):
    def post(self, request):
        error_data = {
            "gu_seq": -1
        }

        id1 = request.data['gu_id']
        pw = request.data['gu_pw']
        try:
            user1 = user.objects.get(gu_id=id1, gu_pw=pw)
            serializer_user = LoginSerializer(user1)
        except:
            return JsonResponse(error_data)

        return Response(serializer_user.data)


# user의 detail을 보여주는 역할
class Groad_user_Detail(APIView):

    def get_object(self, pk):
        user1 = get_object_or_404(user, pk=pk)
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        user1 = self.get_object(pk)
        serializer = UserSerializer(user1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(success_code)
        return JsonResponse(error_code)

    def delete(self, request, pk):
        success_code = {
            'code': 200
        }
        pedometer1 = self.get_object(pk)
        pedometer1.delete()
        return JsonResponse(success_code)


# pedometer의 목록을 보여주는 역할
class Groad_pedometer_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_pedometer")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }

        data = json.loads(request.body)
        gp_step = data.get('gp_step')
        gp_gu_seq_id = data.get('gp_gu_seq_id')

        sql = f"""INSERT INTO groad_pedometer(gp_step,gp_gu_seq_id)
            value('{gp_step}','{gp_gu_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# pedometer의 detail을 보여주는 역할
class Groad_pedometer_Detail(APIView):
    def get(self, request, fk):
        sql = f"""SELECT gp_seq, gp_step, gp_step, gp_gu_seq_id FROM groad_pedometer INNER JOIN groad_user 
        ON gp_gu_seq_id=gu_seq WHERE gp_gu_seq_id={fk}
        """

        try:
            cur = connection.cursor()

            cur.execute(sql)
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        data = json.loads(request.body)
        gp_step = data.get('gp_step')
        gp_gu_seq_id = data.get('gp_gu_seq_id')

        sql = f"""UPDATE groad_pedometer SET gp_step='{gp_step}',gp_gu_seq_id='{gp_gu_seq_id}' WHERE gp_gu_seq_id={fk}"""
        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)

    def delete(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        sql = f"""DELETE FROM groad_pedometer WHERE gp_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# review의 목록을 보여주는 역할
class Groad_review_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_review")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }

        data = json.loads(request.body)
        gr_nickname = data.get('gr_nickname')
        gr_place = data.get('gr_place')
        gr_comment = data.get('gr_comment')
        gr_grade = data.get('gr_grade')
        gr_gu_seq_id = data.get('gr_gu_seq_id')

        sql = f"""INSERT INTO groad_review(gr_nickname, gr_place, gr_comment, gr_grade, gr_gu_seq_id)
            value('{gr_nickname}','{gr_place}','{gr_comment}','{gr_grade}','{gr_gu_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# review의 detail을 보여주는 역할
class Groad_review_Detial(APIView):
    def get(self, request, fk):
        sql = f"""SELECT gr_seq, gr_nickname, gr_place, gr_comment, gr_grade, gr_gu_seq_id FROM groad_review INNER JOIN groad_user 
        ON gr_gu_seq_id=gu_seq WHERE gr_gu_seq_id={fk}
        """

        try:
            cur = connection.cursor()

            cur.execute(sql)
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        data = json.loads(request.body)
        gr_nickname = data.get('gr_nickname')
        gr_place = data.get('gr_place')
        gr_comment = data.get('gr_comment')
        gr_grade = data.get('gr_grade')
        gr_gu_seq_id = data.get('gr_gu_seq_id')

        sql = f"""UPDATE groad_review SET 
        gr_nickname='{gr_nickname}',gr_place='{gr_place}', gr_comment='{gr_comment}', gr_grade='{gr_grade}', gr_gu_seq_id = '{gr_gu_seq_id}' 
        WHERE gr_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)

    def delete(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        sql = f"""DELETE FROM groad_review WHERE gr_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# alarm의 목록을 보여주는 역할
class Groad_alarm_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_alarm")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }

        data = json.loads(request.body)
        ga_onoff1 = data.get('ga_onoff1')
        ga_onoff2 = data.get('ga_onoff2')
        ga_onoff3 = data.get('ga_onoff3')
        ga_gu_seq_id = data.get('ga_gu_seq_id')

        sql = f"""INSERT INTO groad_alarm(ga_onoff1, ga_onoff2, ga_onoff3, ga_gu_seq_id)
            value('{ga_onoff1}','{ga_onoff2}','{ga_onoff3}','{ga_gu_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# alarm의 detail을 보여주는 역할
class Groad_alarm_Detail(APIView):
    def get(self, request, fk):
        sql = f"""SELECT ga_seq, ga_onoff1, ga_onoff2, ga_onoff3, ga_gu_seq_id FROM groad_alarm INNER JOIN groad_user 
        ON ga_gu_seq_id=gu_seq WHERE ga_gu_seq_id={fk}
        """

        try:
            cur = connection.cursor()

            cur.execute(sql)
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        data = json.loads(request.body)
        ga_onoff1 = data.get('ga_onoff1')
        ga_onoff2 = data.get('ga_onoff2')
        ga_onoff3 = data.get('ga_onoff3')
        ga_gu_seq_id = data.get('ga_gu_seq_id')

        sql = f"""UPDATE groad_alarm SET 
        ga_onoff1='{ga_onoff1}',ga_onoff2='{ga_onoff2}', ga_onoff3='{ga_onoff3}', ga_gu_seq_id='{ga_gu_seq_id}'
        WHERE ga_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)

    def delete(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        sql = f"""DELETE FROM groad_alarm WHERE ga_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# qrcode의 목록을 보여주는 역할
class Groad_qrcode_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_qrcode")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }

        data = json.loads(request.body)
        gq_qrcode = data.get('gq_qrcode')
        gq_gu_seq_id = data.get('gq_gu_seq_id')

        sql = f"""INSERT INTO groad_qrcode(gq_qrcode, gq_gu_seq_id)
            value('{gq_qrcode}','{gq_gu_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# qrcode의 detail을 보여주는 역할
class Groad_qrcode_Detail(APIView):
    def get(self, request, fk):
        sql = f"""SELECT gq_seq, gq_qrcode, gq_gu_seq_id FROM groad_qrcode INNER JOIN groad_user 
           ON gq_gu_seq_id=gu_seq WHERE gq_gu_seq_id={fk}
           """

        try:
            cur = connection.cursor()

            cur.execute(sql)
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        data = json.loads(request.body)
        gq_qrcode = data.get('gq_qrcode')
        gq_gu_seq_id = data.get('gq_gu_seq_id')

        sql = f"""UPDATE groad_qrcode SET 
           gq_qrcode='{gq_qrcode}',gq_gu_seq_id='{gq_gu_seq_id}'
           WHERE gq_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)

    def delete(self, request, fk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        sql = f"""DELETE FROM groad_qrcode WHERE gq_gu_seq_id={fk}"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except:
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)
