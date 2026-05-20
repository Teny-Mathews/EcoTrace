from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random

class AnalyzeWasteView(APIView):
    """
    Mock AI Endpoint: Receives an image and returns a breakdown of volume/carbon metrics.
    """
    def post(self, request, *args, **kwargs):
        waste_image = request.FILES.get('image')
        category = request.data.get('category', 'MIXED')

        if not waste_image:
            return Response({"error": "No image provided for analysis."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a mock volume between 0.5 and 5.0 cubic meters
        estimated_volume = round(random.uniform(0.5, 5.0), 2)

        # Carbon calculation based on coefficients
        mitigation_coefficients = {
            'PLASTIC': 2.5, 'ORGANIC': 1.2, 'E_WASTE': 4.0, 'PAPER': 0.8, 'GLASS': 1.5, 'MIXED': 1.0
        }
        multiplier = mitigation_coefficients.get(category.upper(), 1.0)
        calculated_carbon_offset = round(estimated_volume * 1.5 * multiplier, 2)

        return Response({
            "status": "success",
            "analyzed_category": category,
            "estimated_volume_m3": estimated_volume,
            "carbon_offset_kg": calculated_carbon_offset,
            "message": "Image processed successfully."
        }, status=status.HTTP_200_OK)
