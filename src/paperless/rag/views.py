from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class RagAskView(APIView):
    def post(self, request):
        question = request.data.get("question")
        try:
            response = requests.post(
                "http://rag_service:8001/ask",
                json={"question": question},
                timeout=60
            )
            return Response(response.json())
        except Exception as e:
            return Response({"error": str(e)}, status=500)
