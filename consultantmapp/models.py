
from django.db import models


class Consultant(models.Model):
    consname = models.CharField('Consultant Name', max_length=200)
    consemail = models.EmailField('Email Address')
    desireperm = models.CharField('Desire Permanent', max_length=200)
    add_date = models.DateTimeField('Date Added')

    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.consname

class Skill(models.Model):
    skillname = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added')
    last_updated = models.DateTimeField('date updated')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.skillname



class SkillLevel(models.Model):
    skilllevel = models.CharField(max_length=200, unique='true')
    skilltemp = models.CharField(max_length=200)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.skilllevel



class ConsSkill(models.Model):
    consultant = models.ForeignKey(Consultant)
    skill = models.ForeignKey(Skill)
    skilllevel = models.ForeignKey(SkillLevel)
    added_date = models.DateTimeField('Date Added')
    
    def __unicode__(self):
        return u'%s, %s' % (self.consultant, self.skill)

    class Meta:
        verbose_name =  "Consultant Skill"





class Contact(models.Model):
    cosultant = models.ForeignKey(Consultant)
    contactdate = models.DateTimeField('date contact made')
    contacttype = models.CharField('Contact Type', max_length=200)
    whomade = models.CharField('Who made?', max_length = 200)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s, %s' % (self.contacttype, self.contactdate)


