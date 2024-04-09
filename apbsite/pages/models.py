# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WpActionschedulerActions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    hook = models.CharField(max_length=191)
    status = models.CharField(max_length=20)
    scheduled_date_gmt = models.DateTimeField()
    scheduled_date_local = models.DateTimeField()
    args = models.CharField(max_length=191, blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    group_id = models.PositiveBigIntegerField()
    attempts = models.IntegerField()
    last_attempt_gmt = models.DateTimeField()
    last_attempt_local = models.DateTimeField()
    claim_id = models.PositiveBigIntegerField()
    extended_args = models.CharField(max_length=8000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wp_actionscheduler_actions'


class WpActionschedulerClaims(models.Model):
    claim_id = models.BigAutoField(primary_key=True)
    date_created_gmt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_claims'


class WpActionschedulerGroups(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_groups'


class WpActionschedulerLogs(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    action_id = models.PositiveBigIntegerField()
    message = models.TextField()
    log_date_gmt = models.DateTimeField()
    log_date_local = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_actionscheduler_logs'


class WpAi1EcEventCategoryMeta(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    term_color = models.CharField(max_length=255)
    term_image = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_ai1ec_event_category_meta'


class WpAi1EcEventInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_ai1ec_event_instances'
        unique_together = (('post_id', 'start'),)


class WpAi1EcEvents(models.Model):
    post_id = models.BigIntegerField(primary_key=True)
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField(blank=True, null=True)
    timezone_name = models.CharField(max_length=50, blank=True, null=True)
    allday = models.IntegerField()
    instant_event = models.IntegerField()
    recurrence_rules = models.TextField(blank=True, null=True)
    exception_rules = models.TextField(blank=True, null=True)
    recurrence_dates = models.TextField(blank=True, null=True)
    exception_dates = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=32, blank=True, null=True)
    show_map = models.IntegerField(blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=32, blank=True, null=True)
    contact_email = models.CharField(max_length=128, blank=True, null=True)
    contact_url = models.CharField(max_length=255, blank=True, null=True)
    cost = models.CharField(max_length=255, blank=True, null=True)
    ticket_url = models.CharField(max_length=255, blank=True, null=True)
    ical_feed_url = models.CharField(max_length=255, blank=True, null=True)
    ical_source_url = models.CharField(max_length=255, blank=True, null=True)
    ical_organizer = models.CharField(max_length=255, blank=True, null=True)
    ical_contact = models.CharField(max_length=255, blank=True, null=True)
    ical_uid = models.CharField(max_length=255, blank=True, null=True)
    show_coordinates = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    force_regenerate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_ai1ec_events'


class WpAiowpsAuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    network_id = models.BigIntegerField()
    site_id = models.BigIntegerField()
    username = models.CharField(max_length=60)
    ip = models.CharField(max_length=45)
    level = models.CharField(max_length=25)
    event_type = models.CharField(max_length=25)
    details = models.TextField()
    stacktrace = models.TextField()
    created = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_audit_log'


class WpAiowpsDebugLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    level = models.CharField(max_length=25)
    message = models.TextField()
    type = models.CharField(max_length=25)
    created = models.DateTimeField()
    network_id = models.BigIntegerField()
    site_id = models.BigIntegerField()
    logtime = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_debug_log'


class WpAiowpsEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_type = models.CharField(max_length=150)
    username = models.CharField(max_length=150, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    event_date = models.DateTimeField()
    ip_or_host = models.CharField(max_length=100, blank=True, null=True)
    referer_info = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    event_data = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=50, blank=True, null=True)
    created = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_events'


class WpAiowpsGlobalMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    date_time = models.DateTimeField()
    meta_key1 = models.CharField(max_length=255)
    meta_key2 = models.CharField(max_length=255)
    meta_key3 = models.CharField(max_length=255)
    meta_key4 = models.CharField(max_length=255)
    meta_key5 = models.CharField(max_length=255)
    meta_value1 = models.CharField(max_length=255)
    meta_value2 = models.TextField()
    meta_value3 = models.TextField()
    meta_value4 = models.TextField()
    meta_value5 = models.TextField()
    created = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_global_meta'


class WpAiowpsLoggedInUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=60)
    ip_address = models.CharField(max_length=45)
    site_id = models.BigIntegerField()
    created = models.PositiveIntegerField(blank=True, null=True)
    expires = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_logged_in_users'


class WpAiowpsLoginLockdown(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_login = models.CharField(max_length=150)
    lockdown_date = models.DateTimeField()
    release_date = models.DateTimeField()
    failed_login_ip = models.CharField(max_length=100)
    lock_reason = models.CharField(max_length=128)
    unlock_key = models.CharField(max_length=128)
    is_lockout_email_sent = models.IntegerField()
    backtrace_log = models.TextField()
    ip_lookup_result = models.TextField(blank=True, null=True)
    created = models.PositiveIntegerField(blank=True, null=True)
    released = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_login_lockdown'


class WpAiowpsMessageStore(models.Model):
    id = models.BigAutoField(primary_key=True)
    message_key = models.TextField()
    message_value = models.TextField()
    created = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_message_store'


class WpAiowpsPermanentBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    blocked_ip = models.CharField(max_length=100)
    block_reason = models.CharField(max_length=128)
    country_origin = models.CharField(max_length=50)
    blocked_date = models.DateTimeField()
    unblock = models.IntegerField()
    created = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_aiowps_permanent_block'


class WpCntctfrmField(models.Model):
    # id = models.AutoField(unique=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wp_cntctfrm_field'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpCustomizeadmin(models.Model):
    parent_slug = models.CharField(max_length=255, blank=True, null=True)
    menu_title = models.CharField(max_length=255, blank=True, null=True)
    capability = models.CharField(max_length=255, blank=True, null=True)
    menu_slug = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    order_index = models.IntegerField(blank=True, null=True)
    link_target = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_customizeadmin'


class WpDb7Forms(models.Model):
    form_id = models.BigAutoField(primary_key=True)
    form_post_id = models.BigIntegerField()
    form_value = models.TextField()
    form_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_db7_forms'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191, blank=True, null=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'

    def __str__(self):
        return self.option_name

class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpSnippets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    code = models.TextField()
    tags = models.TextField()
    scope = models.CharField(max_length=15)
    priority = models.SmallIntegerField()
    active = models.IntegerField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_snippets'


class WpSupsysticTblColumns(models.Model):
    table_id = models.PositiveIntegerField(blank=True, null=True)
    index = models.PositiveIntegerField()
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_columns'


class WpSupsysticTblConditions(models.Model):
    table_id = models.PositiveIntegerField(blank=True, null=True)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_conditions'


class WpSupsysticTblDiagrams(models.Model):
    table_id = models.PositiveIntegerField(blank=True, null=True)
    start_row = models.PositiveIntegerField(blank=True, null=True)
    start_col = models.PositiveIntegerField(blank=True, null=True)
    end_row = models.PositiveIntegerField(blank=True, null=True)
    end_col = models.PositiveIntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_diagrams'


class WpSupsysticTblRows(models.Model):
    table_id = models.PositiveIntegerField(blank=True, null=True)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_rows'


class WpSupsysticTblRowsHistory(models.Model):
    user_id = models.PositiveIntegerField()
    table_id = models.PositiveIntegerField()
    data = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_rows_history'


class WpSupsysticTblTables(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    meta = models.TextField(blank=True, null=True)
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_supsystic_tbl_tables'


class WpTermRelationships(models.Model):
    object_id = models.PositiveBigIntegerField(primary_key=True)  # The composite primary key (object_id, term_taxonomy_id) found, that is not supported. The first column is selected.
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWcAdminNoteActions(models.Model):
    action_id = models.BigAutoField(primary_key=True)
    note_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    query = models.TextField()
    status = models.CharField(max_length=255)
    is_primary = models.IntegerField()
    actioned_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_wc_admin_note_actions'


class WpWcAdminNotes(models.Model):
    note_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    locale = models.CharField(max_length=20)
    title = models.TextField()
    content = models.TextField()
    icon = models.CharField(max_length=200)
    content_data = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_reminder = models.DateTimeField(blank=True, null=True)
    is_snoozable = models.IntegerField()
    layout = models.CharField(max_length=20)
    image = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_admin_notes'


class WpWcCategoryLookup(models.Model):
    category_tree_id = models.PositiveBigIntegerField(primary_key=True)  # The composite primary key (category_tree_id, category_id) found, that is not supported. The first column is selected.
    category_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_category_lookup'
        unique_together = (('category_tree_id', 'category_id'),)


class WpWcCustomerLookup(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=60)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True, null=True)
    date_last_active = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=2)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'wp_wc_customer_lookup'


class WpWcDownloadLog(models.Model):
    download_log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    permission_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_download_log'


class WpWcOrderCouponLookup(models.Model):
    order_id = models.PositiveBigIntegerField(primary_key=True)  # The composite primary key (order_id, coupon_id) found, that is not supported. The first column is selected.
    coupon_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    discount_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_coupon_lookup'
        unique_together = (('order_id', 'coupon_id'),)


class WpWcOrderProductLookup(models.Model):
    order_item_id = models.PositiveBigIntegerField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    product_id = models.PositiveBigIntegerField()
    variation_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    product_qty = models.IntegerField()
    product_net_revenue = models.FloatField()
    product_gross_revenue = models.FloatField()
    coupon_amount = models.FloatField()
    tax_amount = models.FloatField()
    shipping_amount = models.FloatField()
    shipping_tax_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_product_lookup'


class WpWcOrderStats(models.Model):
    order_id = models.PositiveBigIntegerField(primary_key=True)
    parent_id = models.PositiveBigIntegerField()
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    num_items_sold = models.IntegerField()
    total_sales = models.FloatField()
    tax_total = models.FloatField()
    shipping_total = models.FloatField()
    net_total = models.FloatField()
    returning_customer = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=200)
    customer_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_stats'


class WpWcOrderTaxLookup(models.Model):
    order_id = models.PositiveBigIntegerField(primary_key=True)  # The composite primary key (order_id, tax_rate_id) found, that is not supported. The first column is selected.
    tax_rate_id = models.PositiveBigIntegerField()
    date_created = models.DateTimeField()
    shipping_tax = models.FloatField()
    order_tax = models.FloatField()
    total_tax = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wp_wc_order_tax_lookup'
        unique_together = (('order_id', 'tax_rate_id'),)


class WpWcProductMetaLookup(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    virtual = models.IntegerField(blank=True, null=True)
    downloadable = models.IntegerField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    onsale = models.IntegerField(blank=True, null=True)
    stock_quantity = models.FloatField(blank=True, null=True)
    stock_status = models.CharField(max_length=100, blank=True, null=True)
    rating_count = models.BigIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    total_sales = models.BigIntegerField(blank=True, null=True)
    tax_status = models.CharField(max_length=100, blank=True, null=True)
    tax_class = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_product_meta_lookup'


class WpWcReservedStock(models.Model):
    order_id = models.BigIntegerField(primary_key=True)  # The composite primary key (order_id, product_id) found, that is not supported. The first column is selected.
    product_id = models.BigIntegerField()
    stock_quantity = models.FloatField()
    timestamp = models.DateTimeField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_wc_reserved_stock'
        unique_together = (('order_id', 'product_id'),)


class WpWcTaxRateClasses(models.Model):
    tax_rate_class_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_wc_tax_rate_classes'


class WpWcWebhooks(models.Model):
    webhook_id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=200)
    name = models.TextField()
    user_id = models.PositiveBigIntegerField()
    delivery_url = models.TextField()
    secret = models.TextField()
    topic = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_modified_gmt = models.DateTimeField()
    api_version = models.SmallIntegerField()
    failure_count = models.SmallIntegerField()
    pending_delivery = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_webhooks'


class WpWfblockediplog(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase. The composite primary key (IP, unixday, blockType) found, that is not supported. The first column is selected.
    countrycode = models.CharField(db_column='countryCode', max_length=2)  # Field name made lowercase.
    blockcount = models.PositiveIntegerField(db_column='blockCount')  # Field name made lowercase.
    unixday = models.PositiveIntegerField()
    blocktype = models.CharField(db_column='blockType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfblockediplog'
        unique_together = (('ip', 'unixday', 'blocktype'),)


class WpWfblocks7(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.PositiveIntegerField()
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    blockedtime = models.BigIntegerField(db_column='blockedTime')  # Field name made lowercase.
    reason = models.CharField(max_length=255)
    lastattempt = models.PositiveIntegerField(db_column='lastAttempt', blank=True, null=True)  # Field name made lowercase.
    blockedhits = models.PositiveIntegerField(db_column='blockedHits', blank=True, null=True)  # Field name made lowercase.
    expiration = models.PositiveBigIntegerField()
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfblocks7'


class WpWfconfig(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    val = models.TextField(blank=True, null=True)
    autoload = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wp_wfconfig'


class WpWfcrawlers(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase. The composite primary key (IP, patternSig) found, that is not supported. The first column is selected.
    patternsig = models.CharField(db_column='patternSig', max_length=16)  # Field name made lowercase.
    status = models.CharField(max_length=8)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.
    ptr = models.CharField(db_column='PTR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfcrawlers'
        unique_together = (('ip', 'patternsig'),)


class WpWffilechanges(models.Model):
    filenamehash = models.CharField(db_column='filenameHash', primary_key=True, max_length=64)  # Field name made lowercase.
    file = models.CharField(max_length=1000)
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_wffilechanges'


class WpWffilemods(models.Model):
    filenamemd5 = models.CharField(db_column='filenameMD5', primary_key=True, max_length=16)  # Field name made lowercase.
    filename = models.CharField(max_length=1000)
    real_path = models.TextField()
    knownfile = models.PositiveIntegerField(db_column='knownFile')  # Field name made lowercase.
    oldmd5 = models.CharField(db_column='oldMD5', max_length=16)  # Field name made lowercase.
    newmd5 = models.CharField(db_column='newMD5', max_length=16)  # Field name made lowercase.
    shac = models.CharField(db_column='SHAC', max_length=32)  # Field name made lowercase.
    stoppedonsignature = models.CharField(db_column='stoppedOnSignature', max_length=255)  # Field name made lowercase.
    stoppedonposition = models.PositiveIntegerField(db_column='stoppedOnPosition')  # Field name made lowercase.
    issafefile = models.CharField(db_column='isSafeFile', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wffilemods'


class WpWfhits(models.Model):
    attacklogtime = models.FloatField(db_column='attackLogTime')  # Field name made lowercase.
    ctime = models.FloatField()
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    jsrun = models.IntegerField(db_column='jsRun', blank=True, null=True)  # Field name made lowercase.
    statuscode = models.IntegerField(db_column='statusCode')  # Field name made lowercase.
    isgoogle = models.IntegerField(db_column='isGoogle')  # Field name made lowercase.
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    newvisit = models.PositiveIntegerField(db_column='newVisit')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    referer = models.TextField(blank=True, null=True)
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(max_length=64)
    actiondescription = models.TextField(db_column='actionDescription', blank=True, null=True)  # Field name made lowercase.
    actiondata = models.TextField(db_column='actionData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfhits'


class WpWfhoover(models.Model):
    owner = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    hostkey = models.CharField(db_column='hostKey', max_length=124, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfhoover'


class WpWfissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfissues'


class WpWfknownfilelist(models.Model):
    path = models.TextField()
    wordpress_path = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfknownfilelist'


class WpWflivetraffichuman(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase. The composite primary key (IP, identifier) found, that is not supported. The first column is selected.
    identifier = models.CharField(max_length=32)
    expiration = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wflivetraffichuman'
        unique_together = (('ip', 'identifier'),)


class WpWflocs(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    ctime = models.PositiveIntegerField()
    failed = models.PositiveIntegerField()
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    countryname = models.CharField(db_column='countryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wflocs'


class WpWflogins(models.Model):
    hitid = models.IntegerField(db_column='hitID', blank=True, null=True)  # Field name made lowercase.
    ctime = models.FloatField()
    fail = models.PositiveIntegerField()
    action = models.CharField(max_length=40)
    username = models.CharField(max_length=255)
    userid = models.PositiveIntegerField(db_column='userID')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ua = models.TextField(db_column='UA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wflogins'


class WpWfls2FaSecrets(models.Model):
    user_id = models.PositiveBigIntegerField()
    secret = models.TextField()
    recovery = models.TextField()
    ctime = models.PositiveIntegerField()
    vtime = models.PositiveIntegerField()
    mode = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'wp_wfls_2fa_secrets'


class WpWflsRoleCounts(models.Model):
    serialized_roles = models.CharField(primary_key=True, max_length=255)  # The composite primary key (serialized_roles, two_factor_inactive) found, that is not supported. The first column is selected.
    two_factor_inactive = models.IntegerField()
    user_count = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfls_role_counts'
        unique_together = (('serialized_roles', 'two_factor_inactive'),)


class WpWflsSettings(models.Model):
    name = models.CharField(primary_key=True, max_length=191)
    value = models.TextField(blank=True, null=True)
    autoload = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'wp_wfls_settings'


class WpWfnotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    new = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    priority = models.IntegerField()
    ctime = models.PositiveIntegerField()
    html = models.TextField()
    links = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_wfnotifications'


class WpWfpendingissues(models.Model):
    time = models.PositiveIntegerField()
    lastupdated = models.PositiveIntegerField(db_column='lastUpdated')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    severity = models.PositiveIntegerField()
    ignorep = models.CharField(db_column='ignoreP', max_length=32)  # Field name made lowercase.
    ignorec = models.CharField(db_column='ignoreC', max_length=32)  # Field name made lowercase.
    shortmsg = models.CharField(db_column='shortMsg', max_length=255)  # Field name made lowercase.
    longmsg = models.TextField(db_column='longMsg', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wfpendingissues'


class WpWfreversecache(models.Model):
    ip = models.CharField(db_column='IP', primary_key=True, max_length=16)  # Field name made lowercase.
    host = models.CharField(max_length=255)
    lastupdate = models.PositiveIntegerField(db_column='lastUpdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wp_wfreversecache'


class WpWfsecurityevents(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    data = models.TextField()
    event_time = models.FloatField()
    state = models.CharField(max_length=7)
    state_timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_wfsecurityevents'


class WpWfsnipcache(models.Model):
    ip = models.CharField(db_column='IP', max_length=45)  # Field name made lowercase.
    expiration = models.DateTimeField()
    body = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wfsnipcache'


class WpWfstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    ctime = models.FloatField()
    level = models.PositiveIntegerField()
    type = models.CharField(max_length=5)
    msg = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'wp_wfstatus'


class WpWftrafficrates(models.Model):
    emin = models.PositiveIntegerField(db_column='eMin', primary_key=True)  # Field name made lowercase. The composite primary key (eMin, IP, hitType) found, that is not supported. The first column is selected.
    ip = models.CharField(db_column='IP', max_length=16)  # Field name made lowercase.
    hittype = models.CharField(db_column='hitType', max_length=3)  # Field name made lowercase.
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wftrafficrates'
        unique_together = (('emin', 'ip', 'hittype'),)


class WpWfwaffailures(models.Model):
    throwable = models.TextField()
    rule_id = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_wfwaffailures'


class WpWoocommerceApiKeys(models.Model):
    key_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=10)
    consumer_key = models.CharField(max_length=64)
    consumer_secret = models.CharField(max_length=43)
    nonces = models.TextField(blank=True, null=True)
    truncated_key = models.CharField(max_length=7)
    last_access = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_api_keys'


class WpWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200)
    attribute_label = models.CharField(max_length=200, blank=True, null=True)
    attribute_type = models.CharField(max_length=20)
    attribute_orderby = models.CharField(max_length=20)
    attribute_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_attribute_taxonomies'


class WpWoocommerceDownloadableProductPermissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    download_id = models.CharField(max_length=36)
    product_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    order_key = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    downloads_remaining = models.CharField(max_length=9, blank=True, null=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(blank=True, null=True)
    download_count = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_downloadable_product_permissions'


class WpWoocommerceLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    level = models.SmallIntegerField()
    source = models.CharField(max_length=200)
    message = models.TextField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_log'


class WpWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    order_item_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_itemmeta'


class WpWoocommerceOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200)
    order_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_items'


class WpWoocommercePaymentTokenmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    payment_token_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokenmeta'


class WpWoocommercePaymentTokens(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=200)
    token = models.TextField()
    user_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=200)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokens'


class WpWoocommerceSessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    session_key = models.CharField(unique=True, max_length=32)
    session_value = models.TextField()
    session_expiry = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_sessions'


class WpWoocommerceShippingZoneLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    zone_id = models.PositiveBigIntegerField()
    location_code = models.CharField(max_length=200)
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_locations'


class WpWoocommerceShippingZoneMethods(models.Model):
    zone_id = models.PositiveBigIntegerField()
    instance_id = models.BigAutoField(primary_key=True)
    method_id = models.CharField(max_length=200)
    method_order = models.PositiveBigIntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_methods'


class WpWoocommerceShippingZones(models.Model):
    zone_id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200)
    zone_order = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zones'


class WpWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=200)
    tax_rate_id = models.PositiveBigIntegerField()
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rate_locations'


class WpWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigAutoField(primary_key=True)
    tax_rate_country = models.CharField(max_length=2)
    tax_rate_state = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=8)
    tax_rate_name = models.CharField(max_length=200)
    tax_rate_priority = models.PositiveBigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.PositiveBigIntegerField()
    tax_rate_class = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rates'


class WpWpadmGaCache(models.Model):
    query = models.TextField()
    html = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    request_type = models.CharField(max_length=20, blank=True, null=True)
    object_type = models.CharField(max_length=20, blank=True, null=True)
    clearable = models.IntegerField(blank=True, null=True)
    expired_in = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wpadm_ga_cache'
