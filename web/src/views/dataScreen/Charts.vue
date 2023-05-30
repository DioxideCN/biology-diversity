<template>
    <div ref="main" class="echarts"></div>
</template>

<script lang="ts" setup>
import { ref, onMounted,watch } from "vue";
import * as echarts from "echarts";
import {  GetChart } from './api';
    const main = ref(); // 使用ref创建虚拟DOM引用，使用时用main.value
    let datas = ref([]);
    onMounted(
      () => {
        init();
      }
    );

    function init() {
      // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(main.value);
      // 指定图表的配置项和数据
      GetChart().then((res) =>{
        datas.value=Object.values(res);
        // console.log(datas,res,'res6');
            myChart.setOption({
        color: 'white',
        legend:{
        show:false
        },
        xAxis: {
        type:'category',
        axisTick: {
        alignWithLabel: true
        },
        axisLabel: {
            show: true,
            interval:0,
            rotate:40,
            textStyle: {
            color: 'white',
        }
        },
        data: ['1月份', '2月份', '3月份', '4月份', '5月份', '6月份','7月份','8月份','9月份','10月份','11月份','12月份']
          
        },
        yAxis: {
        type: 'value',
        axisLine:{
            show:true,
        },
        axisLabel: {
            textStyle: {
            color: 'white',
            },
            formatter: function (value, index) {
        // value大于1000时除以1000并拼接k，小于1000按原格式显示
            if (value >= 1000) {
              value = value / 1000 + "k";
            }else if(value < 1000){
              value;
            }
            return value;
            },
        },
        splitNumber: 5,
        // min: 0,
        // max: 700,
        position: 'left',
        },
        series: [
          {
          
            type: 'line',
            smooth: true,
            data: datas.value,
            // data: [50, 200, 360, 600, 100, 620,421,621,333,133,644,324],
            label: {
              lineHeight: 120
            },
            itemStyle: {
            color: "rgba(0, 227, 110, 1)",
            showAllSymbol: true,
            }
          }
        ]
      });
        });
    }
</script>
<style scoped>
.echarts{
    position: absolute;
    left: -1px;
    top: -1px;
    width: 370px;
    height: 290px;
    padding: 10px;
}
</style>