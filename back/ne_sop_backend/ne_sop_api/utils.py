from pathlib import Path, PurePath
from django.template import loader
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


class Utils(object):

    @classmethod
    def set_model_record(cls, record, params):
        """
        Set model record
        """
        atts = cls.get_model_record_attributes(record)

        for att in atts:
            if att != 'affaire_doc_file':
                val = params[att] if att in params else getattr(record, att)

                # Check boolean
                if val == 'true':
                    val = True
                if val == 'false':
                    val = False
                if val == "null" or val == "":
                    val = None

                setattr(record, att, val)

        return record

    @classmethod
    def iterateFilename(cls, filepath):
        count = 0
        filepath_ = filepath
        while Path(filepath_).exists():
            count += 1
            filepath_ = PurePath( f'_{count}.'.join(str(filepath).rsplit('.', 1)) )
        return filepath_
    
    @classmethod
    def get_upload_path(cls, instance, filename):
        return PurePath(str(instance.item.created.year), str(instance.item.id), filename)
    
    @classmethod
    def get_next_documentVersion(cls, DocumentModel, data):
        documents = DocumentModel.objects.filter(
            item=data['item'],
            template=data['template']
        ).all().order_by("-version")

        version = 1
        if len(documents) > 0:
            version = documents[0].version + 1
        
        return version


    @classmethod
    def itemCreatedNotification(cls, item, request):
        template = loader.get_template("email_update_item_fr-ch.html")

        context = {
            'item_id': item.id,
            'item_name': item.title,
            'front_url': settings.FRONT_URL,
        }
        
        return template.render(context, request) 


    @classmethod
    def itemChangedNotification(cls, item, request):
        template = loader.get_template("email_update_item_fr-ch.html")

        context = {
            'item_id': item.id,
            'item_name': item.title,
            'front_url': settings.FRONT_URL,
        }
        
        subject = f"SOP - modification de l'op {item.id}, to={item.user_lead}, cc={item.users_support}"
        body = template.render(context, request)
        to = ['marc.rufener@ne.ch']
        cc = ['marc.rufener@ne.ch']
        # to = item.user_lead
        # cc = item.users_support

        # cls.sendEmailNotification(subject=subject, body=body, to=to, cc=cc)

        return template.render(context, request) 
    
    
    @classmethod
    def sendEmailNotification(cls, subject, body, to, cc=None, bcc=None):
        msg = EmailMultiAlternatives(
            subject=subject,
            body=body,
            from_email="noreply-sop@ne.ch",
            to=to,
            cc=cc,
            bcc=bcc,
        )
        msg.content_subtype="html"
        msg.send()
        return