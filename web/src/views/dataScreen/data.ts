<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>form表单</title>
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" type="text/css" href="https://www.layuicdn.com/layui/css/layui.css" />
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdn.bootcdn.net/ajax/libs/layui/2.6.8/layui.min.js"></script>
</head>
<style>
    html,
    body {
        height: 100%;
    }

    .myTable {
        width: 1200px;
        height: 600px;
        margin: 0 auto;
        border: 1px #eee double;
        box-sizing: border-box;
    }

    .t-header {
        height: 50px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    .t-main {
        height: 50px;
        display: flex;
        align-items: center;
        background-color: #eee;
    }

    .myTable .t-main span {
        width: 16%;
        display: inline-block;
        box-sizing: border-box;
        margin: 10px;
        text-align: center;
    }

    .myTable .layui-input {
        width: 16%;
        display: inline-block;
        box-sizing: border-box;
        margin: 10px 5px;
    }

    .delItem {
        margin-left: 40px;
    }

    .t-footer {
        height: 500px;
        overflow: auto;
    }
</style>

<body>
<div class="myTable">
    <!-- 按钮 -->
    <header class="t-header">
        <button type="button" class="layui-btn subBtn">保存</button>
        <button type="button" class="layui-btn addBtn">新增</button>
    </header>
    <!-- 表头 -->
    <main class="t-main">
        <span>name</span>
        <span>nodeId</span>
        <span>dataMode</span>
        <span>dataType</span>
        <span>sampleRate</span>
        <span>操作</span>
    </main>
    <!-- 模板 -->
    <section class="t-section" style="display: none">
        <form class="layui-form">
            <input type="text" name="name" class="layui-input" placeholder="请输入名称" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="nodeId" class="layui-input" placeholder="请输入nodeId" autocomplete="off" lay-verify="required">
            <input type="text" name="dataMode" class="layui-input" placeholder="请输入dataMode" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="dataType" class="layui-input" placeholder="请输入dataType" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="sampleRate" class="layui-input" placeholder="请输入sampleRate" autocomplete="off" lay-verify="required">
            <button type="button" class="layui-btn layui-btn-primary layui-border-red delItem"
                    onclick="delrow(this)">删除</button>
            <button type="submit" class="layui-btn layui-hide subItem" lay-submit="" lay-filter="subItem">提交</button>
        </form>
    </section>
    <!-- 表单 -->
    <footer class="t-footer">
        <form class="layui-form" lay-filter="f0">
            <input type="text" name="name" class="layui-input" placeholder="请输入名称" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="nodeId" class="layui-input" placeholder="请输入nodeId" autocomplete="off" lay-verify="required">
            <input type="text" name="dataMode" class="layui-input" placeholder="请输入dataMode" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="dataType" class="layui-input" placeholder="请输入dataType" autocomplete="off"
                   lay-verify="required">
            <input type="text" name="sampleRate" class="layui-input" placeholder="请输入sampleRate" autocomplete="off" lay-verify="required">
            <button type="button" class="layui-btn layui-btn-primary layui-border-red delItem"
                    onclick="delrow(this)">删除</button>
            <button type="submit" class="layui-btn layui-hide subItem" lay-submit="" lay-filter="subItem">提交</button>
        </form>
    </footer>
</div>
</body>
<script>
    $(function () {
        layui.use(['element', 'form', 'table', 'layer', 'laydate', 'util'], function () {
            let form = layui.form;
            let table = layui.table;
            let layer = layui.layer;
            let laydate = layui.laydate;
            let element = layui.element;

            //监听提交
            let sum = 0;
            form.on('submit(subItem)', function () {
                sum++
                let length = $(".t-footer form").length; //当前条数
                if (sum == length) {
                    let formData = []
                    for (var i = 0; i < sum; i++) {
                        formData = formData.concat(form.val(`f${i}`))
                    }
                    console.log('formData: ', formData);
                }
                return false;
            });

            // 提交全部
            $('.subBtn').on('click', function () {
                sum = 0;
                $('.t-footer .subItem').trigger('click');
            })

            // 添加行
            let maxCount = 10; //最大行数
            $('.addBtn').on('click', function () {
                let length = $(".t-footer form").length; //当前条数
                if (length < maxCount) { //点击时候，如果当前的数字小于递增结束的条件
                    $(".t-section form").clone().appendTo(".t-footer"); //在表格后面添加一行
                    changeIndex()
                } else {
                    layer.msg(`最多只能添加${maxCount}行`)
                }
            })

            // 删除行
            delrow = function (row) {
                let length = $(".t-footer form").length; //当前条数
                if (length <= 1) {
                    alert("至少保留一行");
                } else {
                    $(row).parent().remove(); //移除当前行
                    changeIndex();
                }
            }
            // 改变序列号
            function changeIndex() {
                let n = 0;
                $(".t-footer form").each(function () {
                    $(this).attr('lay-filter', `f${n++}`)
                });
            }
        });
    });
</script>

</html>
