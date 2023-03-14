from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import NoteSerializer
from .models import Notes 
from django.shortcuts import render
import qrcode
import qrcode.image.pil
from PIL import Image



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getRoutes(request):

    routes = [
        {
            'id':'1',
            'nom':'Med',
            'prenom':'Ali'
        },
        {
            'id':'2',
            'nom':'Hmed',
            'prenom':'Alioune'
        },
        {
            'id':'3',
            'nom':'MedSalem',
            'prenom':'Ahmed'
        },
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createNote(request):

    data = request.data

    note = Notes.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateNote(request, pk):

    data = request.data

    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def deletenote(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()

    return Response('Deleted')

def qr_code_view(request):
    # Générer le code QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    qr.add_data('http://example.com')
    qr.make(fit=True)
    #img = qr.make_image(image_factory=qrcode.image.pil.PilImage)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('code.png')
    # Afficher la page à imprimer avec le code QR
    context = {'img': img}
    return render(request, 'print_page.html', context)
                      


