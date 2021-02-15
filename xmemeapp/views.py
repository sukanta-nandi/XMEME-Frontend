from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import memePostForm, editForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import DeleteView 
import requests
import json
import os

# Create your views here.

BACKEND_URL = 'https://xmemebackendapp.herokuapp.com/memes/'
#BACKEND_URL = 'http://127.0.0.1:7000/memes/'


#Home view form xmeme to handle 
class homeView(View):
    """Handles the home view of xmeme"""

    form_class = memePostForm
    initial = {'key' : 'value'}
    home_template = 'xmemeapp/home.html'



    def get(self, request):
        """fetches memes from the backend"""
        form = self.form_class(initial=self.initial)

        memes = requests.get(BACKEND_URL)
        memes_data = json.loads(memes.content)
        
        context = {
            'memes' : memes_data,
            'memeform' : form,
        }

        return render(request, self.home_template, context)


    def is_url_image(self, image_url):
        """validates a image url"""

        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = requests.head(image_url)

        try:
            if r.headers["content-type"] in image_formats:
                return True
        except:
            return False

    def post(self, request):
        """posts a meme and send it to backend"""
        form = self.form_class(request.POST)
        if form.is_valid():
            memeurl = form.cleaned_data.get('url')

            if self.is_url_image(memeurl):

                response = requests.post(BACKEND_URL, data=request.POST)
                if response.status_code == 201:
                    messages.success(request, 'Your Meme has been posted successfully!')

                else:
                    messages.error(request, 'Unable to post your meme : '+str(response.status_code))
            else :
                messages.error(request, 'Please enter a valid image url')
        else:
            messages.error(request, 'Please Eneter valid details')

        return redirect('home')
        

def deletePost(request, pk):
    """handles deletion  of a post"""

    try :
        response = requests.delete(BACKEND_URL+str(pk)+'/')
        success_msg = 'Successfully deleted your post'
        messages.success(request, success_msg)
    except requests.exceptions.HTTPError as e:
        error_msg = e.response.text
        messages.error(request, error_msg)

    return redirect('home')    


class editView(View):
    """handles editing of a posted meme"""

    form_class = editForm
    initial = {'key' : 'value'}
    edit_template = 'xmemeapp/edit.html'


    

    def get(self, request, pk):
        """Fetches the specific meme data to be edited"""

        meme_json = {}

        try:
            meme = requests.get(BACKEND_URL+str(pk)+'/', timeout=3)
            meme_data = json.loads(meme.content)
            meme_json = meme_data
            editedform = self.form_class(meme_data)
            meme.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            error_msg = "Http Error:"+" Meme does not exist"
            messages.error(request, error_msg)
        except requests.exceptions.ConnectionError as errc:
            error_msg = "Error Connecting:" + errc
            messages.error(request, error_msg)
        except requests.exceptions.Timeout as errt:
            error_msg = "Timeout Error:" + errt
            messages.error(request, error_msg)
        except requests.exceptions.RequestException as err:
            error_msg = "OOps: Some Error occuered" + err
            messages.error(request, error_msg)        


        context = {
            'editform' : editedform,
            'meme' : meme_json
        }

        return render(request, self.edit_template, context)


    def post(self, request, pk):
        """Method for editing updating a meme post"""

        form = self.form_class(request.POST)

        if form.is_valid():
            
            try :
                response = requests.patch(BACKEND_URL+str(pk)+'/', data=request.POST)
                response.raise_for_status()
                success_msg = 'Successfully updated your post'
                messages.success(request, success_msg)
            except requests.exceptions.HTTPError as e:
                error_msg = e.response.text
                messages.error(request, error_msg)
        else :
            error_msg = 'Please Enter valid details'
            messages.error(request, error_msg) 

        return redirect('home')


def sllAuth(request):
    """for verifying ssl"""
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, '.well-known/pki-validation/B49196DA6EF9213ADBB45726509F1A97.txt') 
    data_file = open(file_path , 'r')       
    data = data_file.read()
 
    return HttpResponse(data, content_type='text/json')
