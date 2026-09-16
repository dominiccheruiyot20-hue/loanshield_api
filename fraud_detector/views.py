from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST', 'GET'])
def check_doc(request):
    doc_text = str(request.data.get('text','') if hasattr(request, 'data') else '') + str(request.GET.get('text',''))
    risk = 12
    flags = []
    if 'photoshop' in doc_text.lower() or 'edited' in doc_text.lower():
        risk = 92
        flags.append('Editing software detected')
    if len(doc_text) < 5 and doc_text != '':
        risk = 78
        flags.append('Document too short / incomplete')
    status = 'FAKE' if risk > 50 else 'REAL'
    return Response({'status': status, 'risk_score': risk, 'flags': flags, 'message': f'Checked: {doc_text[:30]}'})

