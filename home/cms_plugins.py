from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Sprint, Process, Tester

class SprintPlugin(CMSPluginBase):
    model = Sprint
    name = _("Sprint Plugin")
    render_template = "sprint_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SprintPlugin, self).render(context, instance, placeholder)
        return context

class TesterPlugin(CMSPluginBase):
    model = Tester
    name = _("Tester Plugin")
    render_template = "tester_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TesterPlugin, self).render(context, instance, placeholder)
        return context


class ProcessPlugin(CMSPluginBase):
    model = Process
    name = _("Process Plugin")
    render_template = "process_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ProcessPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(SprintPlugin)
plugin_pool.register_plugin(TesterPlugin)
plugin_pool.register_plugin(ProcessPlugin)
