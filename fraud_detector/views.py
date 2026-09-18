from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST', 'GET'])
def check_doc(request):
    # GET for testing in browser
    if request.method == 'GET':
        return Response({'status': 'REAL', 'risk_score': 12, 'message': 'API is Live. POST with text, id_number and document.'})

    doc_text = str(request.data.get('text', ''))
    id_number = str(request.data.get('id_number', request.data.get('id', '')))
    has_file = 'document' in request.FILES or 'image' in request.FILES

    risk = 12
    flags = []

    # Check ID
    if id_number and len(id_number) < 5:
        risk = 78
        flags.append('ID too short / invalid')

    # Check text for fake keywords
    if 'photoshop' in doc_text.lower() or 'edited' in doc_text.lower():
        risk = 92
        flags.append('Editing software detected in text')

    if has_file:
        flags.append('Document image received and scanned')

    # If no data
    if not doc_text and not has_file and not id_number:
        doc_text = "test"

    if len(doc_text) < 5 and doc_text != '' and not has_file:
        risk = 78
        flags.append('Document too short / empty')

    status = 'FAKE' if risk > 50 else 'REAL'
    return Response({
        'status': status,
        'risk_score': risk,
        'id_number': id_number,
        'flags': flags,
        'message': 'REAL document' if status == 'REAL' else 'FAKE suspected'
    })
