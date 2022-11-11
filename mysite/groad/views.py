from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.db import connection
from .models import user
import json
from .serializer import UserSerializer, LoginSerializer


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
        (gu_id, gu_pw, gu_name, gu_gender, gu_birth_date, gu_email, gu_phone_number, gu_point_number)
            value('{gu_id}','{gu_pw}','{gu_name}','{gu_gender}','{gu_birth_date}','{gu_email}','{gu_phone_number}',0)
        """
        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except Exception as e:
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
        return user1

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


# inquiry의 목록을 보여주는 역할
class Groad_inquiry_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_inquiry")
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
        gi_title = data.get('gi_title')
        gi_contents = data.get('gi_contents')
        gi_gu_seq_id = data.get('gi_gu_seq_id')

        sql = f"""INSERT INTO groad_inquiry(gi_title, gi_contents, gi_gu_seq_id)
            value('{gi_title}','{gi_contents}','{gi_gu_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# inquiry의 detail을 보여주는 역할
class Groad_inquiry_Detial(APIView):
    def get(self, request, fk):
        sql = f"""SELECT gi_seq, gi_title, gi_contents, gi_gu_seq_id FROM groad_inquiry INNER JOIN groad_user 
        ON gi_gu_seq_id=gu_seq WHERE gi_gu_seq_id={fk}
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
        gr_name = data.get('gr_name')
        gr_place = data.get('gr_place')
        gr_content_text = data.get('gr_content_text')
        gr_grade = data.get('gr_grade')
        gr_date = data.get('gr_date')
        gr_content_image = data.get('gr_content_image')
        gr_profile_image = data.get('gr_profile_image')
        gr_gu_seq_id = data.get('gr_gu_seq_id')

        sql = f"""INSERT INTO groad_review(gr_name, gr_place, gr_content_text, gr_grade, gr_gu_seq_id,gr_date, gr_content_image, gr_profile_image)
            value('{gr_name}','{gr_place}','{gr_content_text}','{gr_grade}','{gr_gu_seq_id}','{gr_date}','{gr_content_image}','{gr_profile_image}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# review의 detail을 보여주는 역할
class Groad_review_Detial(APIView):
    def get(self, request, pk):

        sql = f"""SELECT gr_seq, gr_name, gr_place, gr_content_text, gr_grade, gr_gu_seq_id, gr_date, gr_content_image, gr_profile_image FROM groad_review INNER JOIN groad_user 
        ON gr_gu_seq_id=gu_seq WHERE gr_seq={pk}
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

    def put(self, request, pk):
        error_code = {
            'code': -3
        }
        success_code = {
            'code': 200
        }
        data = json.loads(request.body)
        gr_name = data.get('gr_name')
        gr_place = data.get('gr_place')
        gr_content_text = data.get('gr_content_text')
        gr_grade = data.get('gr_grade')
        gr_date = data.get('gr_date')
        gr_content_image = data.get('gr_content_image')
        gr_profile_image = data.get('gr_profile_image')
        gr_gu_seq_id = data.get('gr_gu_seq_id')

        sql = f"""UPDATE groad_review SET 
        gr_name='{gr_name}',gr_place='{gr_place}', gr_content_text='{gr_content_text}', 
        gr_grade='{gr_grade}',gr_gu_seq_id='{gr_gu_seq_id}',gr_date='{gr_date}',gr_content_image='{gr_content_image}',
        gr_profile_image = '{gr_profile_image}'
        WHERE gr_seq={pk}"""

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


# review_comment 의 목록을 보여주는 역할
class Groad_review_comment_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_review_comment")
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
        grc_name = data.get('grc_name')
        grc_profile_image = data.get('grc_profile_image')
        grc_comment = data.get('grc_comment')
        grc_gr_seq_id = data.get('grc_gr_seq_id')

        sql = f"""INSERT INTO groad_review_comment(grc_name, grc_profile_image, grc_comment, grc_gr_seq_id)
            value('{grc_name}','{grc_profile_image}','{grc_comment}','{grc_gr_seq_id}')"""

        try:
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
        except Exception as e:
            print(e)
            connection.rollback()
            return JsonResponse(error_code)
        finally:
            cur.close()
        return JsonResponse(success_code)


# review_comment 의 detail을 보여주는 역할
class Groad_review_comment_Detial(APIView):
    def get(self, request, fk):
        sql = f"""SELECT grc_seq, grc_name, grc_profile_image, grc_comment, grc_gr_seq_id FROM groad_review_comment INNER JOIN groad_review 
        ON grc_gr_seq_id = gr_seq WHERE grc_gr_seq_id={fk}
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
        grc_name = data.get('grc_name')
        grc_profile_image = data.get('grc_profile_image')
        grc_comment = data.get('grc_comment')
        grc_gr_seq_id = data.get('grc_gr_seq_id')

        sql = f"""UPDATE groad_review_comment SET 
        grc_name='{grc_name}',grc_profile_image='{grc_profile_image}', grc_comment='{grc_comment}', 
        grc_gr_seq_id='{grc_gr_seq_id}'
        WHERE grc_gr_seq_id={fk}"""

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
        sql = f"""DELETE FROM groad_review_comment WHERE grc_gr_seq_id={fk}"""

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


# setting의 목록을 보여주는 역할
class Groad_setting_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_setting")
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
        gs_map = data.get('gs_map')
        gs_theme = data.get('gs_theme')
        gs_onoff1 = data.get('gs_onoff1')
        gs_onoff2 = data.get('gs_onoff2')
        gs_onoff3 = data.get('gs_onoff3')
        gs_gu_seq_id = data.get('gs_gu_seq_id')

        sql = f"""INSERT INTO groad_setting(gs_map, gs_theme, gs_onoff1, gs_onoff2, gs_onoff3, gs_gu_seq_id)
            value('{gs_map}','{gs_theme}','{gs_onoff1}','{gs_onoff2}','{gs_onoff3}','{gs_gu_seq_id}')"""

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


# setting의 detail을 보여주는 역할
class Groad_setting_Detail(APIView):
    def get(self, request, fk):
        sql = f"""SELECT gs_seq, gs_map, gs_theme, gs_onoff1, gs_onoff2, gs_onoff3, gs_gu_seq_id FROM groad_setting INNER JOIN groad_user 
        ON gs_gu_seq_id=gu_seq WHERE gs_gu_seq_id={fk}
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
        gs_map = data.get('gs_map')
        gs_theme = data.get('gs_theme')
        gs_onoff1 = data.get('gs_onoff1')
        gs_onoff2 = data.get('gs_onoff2')
        gs_onoff3 = data.get('gs_onoff3')
        gs_gu_seq_id = data.get('gs_gu_seq_id')

        sql = f"""UPDATE groad_setting SET 
        gs_map = '{gs_map}',gs_theme='{gs_theme}',gs_onoff1='{gs_onoff1}',gs_onoff2='{gs_onoff2}', gs_onoff3='{gs_onoff3}', gs_gu_seq_id='{gs_gu_seq_id}'
        WHERE gs_gu_seq_id={fk}"""

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


# travelcourse 의 목록을 보여주는 역할
class Groad_travelcourse_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_travelcourse")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course1position 의 목록을 보여주는 역할
class Groad_course1position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course1position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course2position 의 목록을 보여주는 역할
class Groad_course2position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course2position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course3position 의 목록을 보여주는 역할
class Groad_course3position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course3position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course4position 의 목록을 보여주는 역할
class Groad_course4position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course4position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course5position 의 목록을 보여주는 역할
class Groad_course5position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course5position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course6position 의 목록을 보여주는 역할
class Groad_course6position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course6position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course7position 의 목록을 보여주는 역할
class Groad_course7position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course7position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course8position 의 목록을 보여주는 역할
class Groad_course8position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course8position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)


# course9position 의 목록을 보여주는 역할
class Groad_course9position_List(APIView):
    def get(self, request):
        try:
            cur = connection.cursor()
            cur.execute("SELECT * FROM groad_course9position")
            result = [dict((cur.description[i][0], value) \
                           for i, value in enumerate(row)) for row in cur.fetchall()]
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        finally:
            cur.close()

        return Response(result, status=status.HTTP_200_OK)
