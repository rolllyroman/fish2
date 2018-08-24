  <div class='block'>
       %include admin_frame_header
       <div class='content'>
          <div id="toolbar" class="btn-group">
               <button id="btn_add" type="button" class="btn btn-sm btn-primary">
                  <span class="glyphicon glyphicon-plus">
                      <a href="{{info['createUrl']}}" style='color:#FFF;text-decoration:none;'>调试预设值</a>
                  </span>
              </button>
          </div>
          <table id='loadDataTable' class="table table-bordered table-hover " ></table>
       </div>
  </div>
<script type="text/javascript">
    /**
      *表格数据
    */
    var editId;        //定义全局操作数据变量
    var isEdit;
    var startDate;
    var endDate;
    $('#loadDataTable').bootstrapTable({
          method: 'get',
          url: "{{info['tableUrl']}}",
          contentType: "application/json",
          datatype: "json",
          cache: false,
          checkboxHeader: true,
          detailView: true,//父子表
          pagination: true,
          pageSize: 16,
          toolbar:'#toolbar',
          pageList: [24, 48, 100,'All'],
          search: true,
          showRefresh: true,
          minimumCountColumns: 2,
          clickToSelect: true,
          smartDisplay: true,
          //sidePagination : "server",
          sortOrder: 'desc',
          sortName: 'datetime',
          //queryParams:getSearchP,
          responseHandler:responseFunc,
          //onLoadError:responseError,
          showExport:true,
          exportTypes:['excel', 'csv', 'pdf', 'json'],
          //exportOptions:{fileName: "{{info['title']}}"+"_"+ new Date().Format("yyyy-MM-dd")},
          columns: [
          [{
                    halign    : "center",
                    font      :  15,
                    align     :  "left",
                    class     :  "totalTitle",
                    colspan   :  12
          }],
          [{
              checkbox: true
          },{
              field: 'diamond_charge_sum',
              title: '钻石充值总额',
              align: 'center',
              valign: 'middle'
          },{

              field: 'diamond_to_coin',
              title: '钻石兑换金币总额',
              align: 'center',
              valign: 'middle'
          },{

              field: 'produce_coin',
              title: '金币场产出金币',
              align: 'center',
              valign: 'middle'
          },{

              field: 'earnings_coin',
              title: '金币场玩家投入金币',
              align: 'center',
              valign: 'middle'
          },{
              field: 'produce_warhead',
              title: '弹头场产出弹头',
              align: 'center',
              valign: 'middle'
          },{
              field: 'earnings_warhead',
              title: '弹头场玩家投入弹头',
              align: 'center',
              valign: 'middle'
          },{
              field: 'coin_rate',
              title: '金币产出投入比',
              align: 'center',
              valign: 'middle'
          },{
              field: 'warhead_rate',
              title: '弹头产出投入比',
              align: 'center',
              valign: 'middle'
		  },{
              field: 'preset_value',
              title: '预设值',
              align: 'center',
              valign: 'middle'
		  },{
              field: 'greater_than',
              title: '大于预设值下的捕获率',
              align: 'center',
              valign: 'middle'
		  },{
              field: 'less_than',
              title: '小于预设值下的捕获率',
              align: 'center',
              valign: 'middle'
          }]],

         //注册加载子表的事件。注意下这里的三个参数！
          onExpandRow: function (index, row, $detail) {
              console.log(index,row,$detail);
              //InitSubTable(index, row, $detail);
          }
      });

        function responseFunc(res){
            console.log("-------------------------data:"+res.data);
            data = res.data;
            count = res.count;
            //$('.totalTitle').html('房间总数: '+count+" 今日新增: 0");
            return data;
        }


</script>
%rebase admin_frame_base
