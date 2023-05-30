<template>
  <div :class="prefixCls">
    <Popover title="" trigger="click" :overlayClassName="`${prefixCls}__overlay`">
      <!-- <Badge :count="count" dot :numberStyle="numberStyle">
        <BellOutlined />
      </Badge> -->
      <template #content>
        <Tabs>
          <template v-for="item in titlelist" :key="item.key">
            <TabPane>
              <template #tab>
                {{ item.name }}
                <span v-if="lists.length !== 0">({{ lists.length }})</span>
              </template>
              <!-- 绑定title-click事件的通知列表中标题是“可点击”的-->
              <NoticeList :list="lists" @title-click="onNoticeClick" />
            </TabPane>
          </template>
        </Tabs>
        <Modal title="详细消息" v-model:visible="visible" @ok="handleOk" @cancel="handleCancel" v-model:tem="tem">
          <div v-for="list in lists" :key="list.id">
            <p v-if="list.id == tem">{{list.message}}</p>
          </div>
        </Modal>
      </template>
    </Popover>
  </div>
</template>
<script lang="ts">
  import { computed, defineComponent, ref, onMounted } from 'vue';
  import { Popover, Tabs, Badge, Modal } from 'ant-design-vue';
  import { BellOutlined } from '@ant-design/icons-vue';
  import { tabListData, ListItem } from './data';
  import NoticeList from './NoticeList.vue';
  import { useDesign } from '/@/hooks/web/useDesign';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { getList } from './data';
  export default defineComponent({
    components: { Popover, Modal, BellOutlined, Tabs, TabPane: Tabs.TabPane, Badge, NoticeList },
    setup() {
      const { prefixCls } = useDesign('header-notify');
      const { createMessage } = useMessage();
      const listData = ref(tabListData);
      const visible = ref(false);
      const lists = ref([]);
      let tem = ref('');
      const titlelist = ref([{
      key: '1',
      name: '消息',
      }])
      const count = ref(1);
      const showModal = () => {
        visible.value = true;
      };

      const handleOk = e => {
        visible.value = false;
      };
      const handleCancel = () => {
        visible.value = false;
      };

      // const count = computed(() => {
      //   let count = 0;
      //   for (let i = 0; i < tabListData.length; i++) {
      //     count += tabListData[i].list.length;
      //   }
      //   return count;
      // });
      function getData() {
        getList({}).then((res) => {
          lists.value = res.items;
        });
      }
      onMounted(() => {
        getData();
      });
      function onNoticeClick(record: ListItem) {
        showModal();
        tem.value = record.id;
        // createMessage.success('你点击了通知，ID=' + record.id);
        // 可以直接将其标记为已读（为标题添加删除线）,此处演示的代码会切换删除线状态
        record.titleDelete = !record.titleDelete;
      }

      return {
        prefixCls,
        listData,
        count,
        onNoticeClick,
        numberStyle: {},
        visible,
        showModal,
        handleOk,
        lists,
        getData,
        titlelist,
        handleCancel,
        tem,
      };
    },
  });
</script>
<style lang="less">
  @prefix-cls: ~'@{namespace}-header-notify';

  .@{prefix-cls} {
    padding-top: 2px;

    &__overlay {
      max-width: 500px;
    }
    .ant-tabs-content {
      width: 500px;
    }

    .ant-badge {
      font-size: 18px;

      .ant-badge-multiple-words {
        padding: 0 4px;
      }

      svg {
        width: 0.9em;
      }
    }
  }
  .ant-popover-inner-content {
   width: 250px;
  }
</style>
