(function () {

    var setup_checkbox_list = function(field_id) {
        var $field_label
          , $field_list
          , $field_display
          , $field
          , $boxes;

        $field = $('#' + field_id);
        $field_label = $('#' + field_id + ' > label');
        $field_list = $('#' + field_id + ' ul');
        $boxes = $field_list.find('input[type="checkbox"]');
        
        // Insert a div to display the current selection(s)
        $field_display = $('<div class="field_selection"></div>');
        $field.prepend($field_display);
        
        $field_list.hide();
        $field_label.click(function() {
            $field_list.slideToggle();
            $field_display.fadeToggle();
            $field.css('min-height', ($field_display.height() + 10) + 'px');
        });

        $boxes.change(function() {
            update_selection_display($boxes, $field_display);
        });
        update_selection_display($boxes, $field_display);
    };
    
    var update_selection_display = function($boxes, $display) {
        var selection = [];
        $boxes.filter(':checked').each(function(i, box) {
            selection[i] = $(box).parent().text().trim();
        });
        $display.html(selection.join(', '));
    };

    var init = function() {
        //setup_checkbox_list('div_id_topics');
        //setup_checkbox_list('div_id_statuses');
        //setup_checkbox_list('div_id_controlling_bodies');
        //setup_checkbox_list('div_id_file_types');
        //setup_checkbox_list('div_id_sponsors');
    };

    $(function() {
        init();
        $(".selectmultiple").chosen({'width' : '100%'});
    });

})();
