from pathlib import Path, PurePath

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader


class Utils(object):
    @classmethod
    def set_model_record(cls, record, params):
        """
        Set model record
        """
        atts = cls.get_model_record_attributes(record)

        for att in atts:
            if att != "affaire_doc_file":
                val = params[att] if att in params else getattr(record, att)

                # Check boolean
                if val == "true":
                    val = True
                if val == "false":
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
            filepath_ = PurePath(f"_{count}.".join(str(filepath).rsplit(".", 1)))
        return filepath_

    @classmethod
    def get_upload_path(cls, instance, filename):
        return PurePath(str(instance.item.created.year), str(instance.item.id), filename)

    @classmethod
    def get_next_documentVersion(cls, DocumentModel, data):
        documents = DocumentModel.objects.filter(item=data["item"], template=data["template"]).all().order_by("-version")

        version = 1
        if len(documents) > 0:
            version = documents[0].version + 1

        return version

    @classmethod
    def itemCreatedNotification(cls, item, request):
        template = loader.get_template("email_create_item_fr-ch.html")

        context = {
            "item_id": item.id,
            "item_name": item.title,
            "front_url": settings.FRONT_URL,
            "main_service": item.get_entity_lead_name(),
            "support_services": item.get_entity_support_name(),
        }

        user_lead_email = item.get_user_lead_email()
        users_support_email = item.get_users_support_email()

        subject = f"SOP - création de l'OP {item.number}"
        body = template.render(context, request)
        to = user_lead_email if user_lead_email is not None else users_support_email
        cc = users_support_email if to is user_lead_email is not None else None

        cls.sendEmailNotification(subject=subject, body=body, to=to, cc=cc)

    @classmethod
    def itemChangedNotification(cls, item, request):
        template = loader.get_template("email_update_item_fr-ch.html")

        context = {
            "item_id": item.id,
            "item_name": item.title,
            "front_url": settings.FRONT_URL,
            "main_service": item.get_entity_lead_name(),
            "support_services": item.get_entity_support_name(),
        }

        user_lead_email = item.get_user_lead_email()
        users_support_email = item.get_users_support_email()

        subject = f"SOP - modification de l'OP {item.number}"
        body = template.render(context, request)
        to = user_lead_email if user_lead_email is not None else users_support_email
        cc = users_support_email if to is user_lead_email is not None else None

        cls.sendEmailNotification(subject=subject, body=body, to=to, cc=cc)

    @classmethod
    def itemRemovedNotification(cls, item, request):
        template = loader.get_template("email_delete_item_fr-ch.html")

        context = {
            "item_name": item.title,
        }

        user_lead_email = item.get_user_lead_email()
        users_support_email = item.get_users_support_email()

        subject = f"SOP - suppression de l'OP {item.number}"
        body = template.render(context, request)
        to = user_lead_email if user_lead_email is not None else users_support_email
        cc = users_support_email if to is user_lead_email is not None else None

        cls.sendEmailNotification(subject=subject, body=body, to=to, cc=cc)

    @classmethod
    def itemLateNotification(cls, item, request):
        template = loader.get_template("email_late_item_fr-ch.html")

        context = {
            "item_id": item.id,
            "item_name": item.title,
            "front_url": settings.FRONT_URL,
            "main_service": item.get_entity_lead_name(),
            "support_services": item.get_entity_support_name(),
        }

        user_lead_email = item.get_user_lead_email()
        users_support_email = item.get_users_support_email()

        subject = f"SOP - retard de traitement de l'OP {item.number}"
        body = template.render(context, request)
        to = user_lead_email if user_lead_email is not None else users_support_email
        cc = users_support_email if to is user_lead_email is not None else None

        cls.sendEmailNotification(subject=subject, body=body, to=to, cc=cc)

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
        msg.content_subtype = "html"
        msg.send()

    @classmethod
    def auto_adjust_excel_column_width(cls, ws):
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter  # Obtenir la lettre de la colonne
            for cell in col:
                try:
                    actual_max_length = max([len(str(s)) for s in cell.value.split("\n")])
                    if actual_max_length > max_length:
                        max_length = actual_max_length
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)  # Ajouter un peu d'espace
            ws.column_dimensions[column].width = adjusted_width
        return ws
