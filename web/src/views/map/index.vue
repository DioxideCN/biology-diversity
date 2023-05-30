<template>
  <div>
    <Modal v-model:visible="visible" title="区域信息更改" @ok="handleOk">
      <div  class="name"
        >区域名称：<a-input v-model:value="areaName" class="inp" placeholder="请输入区域名称"
      /><a-button class="deleteBtn" type="primary" danger @click="deleteArea()">删除该区域</a-button></div>
      
    </Modal>
    <Modal v-model:visible="Pvisible" title="标记信息更改" @ok="PhandleOk">
      <div class="name"
        >标记名称：<a-input v-model:value="pointName" class="inp" placeholder="请输入标记名称"
      /><a-button class="deleteBtn" type="primary" danger @click="deletePoint()">删除该标记</a-button></div>
      
    </Modal>
    <div style="width: 100%; background-color: red; height: 800px" id="map"></div>
  </div>
</template>
<script lang="ts">
import { deleteItem, getList, createOrUpdate, getAllList, getById } from './api';
import { PdeleteItem, PgetList, PcreateOrUpdate, PgetAllList, PgetById } from './PointApi';
import { ref, defineComponent, onMounted, reactive, inject } from 'vue';
import { Progress, Modal, message } from 'ant-design-vue';
import maps from '../../map';
export default defineComponent({
  name: 'Demo',
  components: {
    Progress,
    Modal,
  },
  setup() {
    const refresh = inject('reload');
    let area = reactive({
      arr: [],
    });
    let point = reactive({
      arr: [],
    });
    let areaName = ref('');
    let areaId = ref(-1);
    let areaPath = ref('');
    let pointName = ref('');
    let pointId = ref(-1);
    let pointPath = ref('');
    const modalText = ref<string>('Content of the modal');
    const visible = ref<boolean>(false);
    const Pvisible = ref<boolean>(false);
    const confirmLoading = ref<boolean>(false);

    const showModal = () => {
      visible.value = true;
    };
    const handleOk = () => {
      let params = {
        id: areaId.value,
        name: areaName.value,
        path: areaPath.value,
      };
      createOrUpdate(params, true).then(()=>{
          message.success(`更改成功`);
      });;
      visible.value = false;

      // window.location.reload();
      refresh();
      getArea();
    };
    const PshowModal = () => {
      Pvisible.value = true;
    };
    const PhandleOk = () => {
      let params = {
        id: pointId.value,
        name: pointName.value,
        path: pointPath.value,
      };
      PcreateOrUpdate(params, true).then(()=>{
          message.success(`更改成功`);
      });;
      Pvisible.value = false;

      // window.location.reload();
      refresh();
      getPoint();
    };
    const getArea = () => {
      getAllList().then((res) => {
        area.arr = res.result;
        area.arr.forEach((item) => {
          let polygon = BM.polygon(item['path'], { color: 'red' }).addTo(map);
          polygon.bindTooltip(item['name'], { permanent: true });
          polygon.on('click', function (e) {
            areaName.value = item.name;
            areaId.value = item.id;
            areaPath.value = JSON.stringify(item.path);
            getById(item.id).then((res) => {
              // console.log(res);
            });
            showModal();
          });
        });
      });
    };
    const getPoint = () => {
      PgetAllList().then((res) => {
        point.arr = res.result;
        point.arr.forEach((item) => {
          let marker = BM.marker(item['path']).addTo(map);
          marker.bindTooltip(item['name'], { permanent: true });
          marker.on('click', function (e) {
            pointName.value = item.name;
            pointId.value = item.id;
            pointPath.value = JSON.stringify(item.path);
            PshowModal();
          });
        });
      });
    };
    const deleteArea = () => {
      deleteItem(areaId.value).then(()=>{
        visible.value = false;
        refresh()
          message.success(`删除成功`);
      });;
    }
    const deletePoint = () => {
      PdeleteItem(pointId.value).then(()=>{
        Pvisible.value = false;
        refresh()
          message.success(`删除成功`);
      });;
    }
    onMounted(() => {
      let BM;
      maps.then(() => {
        BM = window.BM;
        BM.Config.HTTP_URL = 'http://localhost:9000';
        let map = BM.map('map', 'bigemap.crhp77pj', {
          center: [37.74539566040039, 119.09660339355469],
          zoom: 5,
          zoomControl: false,
        });
        map.fitBounds([
          [37.638702392578125, 118.89404296875],
          [37.85208511352539, 119.29916381835938],
        ]);
        getAllList().then((res) => {
          area.arr = res.result;
          area.arr.forEach((item) => {
            let polygon = BM.polygon(item['path'], { color: 'red' }).addTo(map);
            polygon.bindTooltip(item['name'], { permanent: true });
            polygon.on('click', function (e) {
              areaName.value = item.name;
              areaId.value = item.id;
              areaPath.value = JSON.stringify(item.path);
              getById(item.id).then((res) => {
                // console.log(res);
              });
              showModal();
            });
          });
        });
        PgetAllList().then((res) => {
          point.arr = res.result;
          point.arr.forEach((item) => {
            let marker = BM.marker(item['path']).addTo(map);
            marker.bindTooltip(item['name'], { permanent: true });
            marker.on('click', function (e) {
              pointName.value = item.name;
              pointId.value = item.id;
              pointPath.value = JSON.stringify(item.path);
              PshowModal();
            });
          });
        });

        //#region
        function _hasAncestor(t, e) {
          for (; (t = t.parentElement) && !t.classList.contains(e); );
          return t;
        }
        (BM.drawVersion = '0.4.2'),
          (BM.Draw = {}),
          (BM.drawLocal = {
            draw: {
              toolbar: {
                actions: {
                  title: '取消',
                  text: '取消',
                },
                finish: {
                  title: '完成',
                  text: '完成',
                },
                undo: {
                  title: '删除最后一个点',
                  text: '删除最后一个点',
                },
                buttons: {
                  // polyline: '线条',
                  polygon: '多边形',
                  // rectangle: '矩形',
                  circle: '圆',
                  marker: '标注',
                  // circlemarker: '圆标注',
                },
              },
              handlers: {
                circle: {
                  tooltip: {
                    start: '单击开始',
                  },
                  radius: '半径',
                },
                circlemarker: {
                  tooltip: {
                    start: '单击地图开始',
                  },
                },
                marker: {
                  tooltip: {
                    start: '单击地图开始',
                  },
                },
                polygon: {
                  tooltip: {
                    start: '单击地图开始',
                    cont: '',
                    end: '双击完成',
                  },
                },
                polyline: {
                  error: '<strong>Error:</strong> 边界出错!',
                  tooltip: {
                    start: '单击地图开始',
                    cont: '',
                    end: '双击点完成',
                  },
                },
                rectangle: {
                  tooltip: {
                    start: '单击地图开始',
                  },
                },
                simpleshape: {
                  tooltip: {
                    end: '松开鼠标结束',
                  },
                },
              },
            },
            edit: {
              toolbar: {
                actions: {
                  save: {
                    title: '保存',
                    text: '保存',
                  },
                  cancel: {
                    title: '取消',
                    text: 'Cancel',
                  },
                  clearAll: {
                    title: '全部取消',
                    text: '全部取消',
                  },
                },
                buttons: {
                  edit: '编辑',
                  editDisabled: '请先选择一个要素',
                  remove: '删除',
                  removeDisabled: '没有删除的要素',
                },
              },
              handlers: {
                edit: {
                  tooltip: {
                    text: '单击定位点来编辑',
                    subtext: '',
                  },
                },
                remove: {
                  tooltip: {
                    text: '删除',
                  },
                },
              },
            },
          }),
          (BM.Draw.Event = {}),
          (BM.Draw.Event.CREATED = 'draw:created'),
          (BM.Draw.Event.EDITED = 'draw:edited'),
          (BM.Draw.Event.DELETED = 'draw:deleted'),
          (BM.Draw.Event.DRAWSTART = 'draw:drawstart'),
          (BM.Draw.Event.DRAWSTOP = 'draw:drawstop'),
          (BM.Draw.Event.DRAWVERTEX = 'draw:drawvertex'),
          (BM.Draw.Event.EDITSTART = 'draw:editstart'),
          (BM.Draw.Event.EDITMOVE = 'draw:editmove'),
          (BM.Draw.Event.EDITRESIZE = 'draw:editresize'),
          (BM.Draw.Event.EDITVERTEX = 'draw:editvertex'),
          (BM.Draw.Event.EDITSTOP = 'draw:editstop'),
          (BM.Draw.Event.DELETESTART = 'draw:deletestart'),
          (BM.Draw.Event.DELETESTOP = 'draw:deletestop'),
          (BM.Draw.Event.TOOLBAROPENED = 'draw:toolbaropened'),
          (BM.Draw.Event.TOOLBARCLOSED = 'draw:toolbarclosed'),
          (BM.Draw.Event.MARKERCONTEXT = 'draw:markercontext'),
          (BM.Draw = BM.Draw || {}),
          (BM.Draw.Feature = BM.Handler.extend({
            initialize: function (t, e) {
              (this._map = t),
                (this._container = t._container),
                (this._overlayPane = t._panes.overlayPane),
                (this._popupPane = t._panes.popupPane),
                e &&
                  e.shapeOptions &&
                  (e.shapeOptions = BM.Util.extend({}, this.options.shapeOptions, e.shapeOptions)),
                BM.setOptions(this, e);
              var i = BM.version.split('.');
              1 === parseInt(i[0], 10) && 2 <= parseInt(i[1], 10)
                ? BM.Draw.Feature.include(BM.Evented.prototype)
                : BM.Draw.Feature.include(BM.Mixin.Events);
            },
            enable: function () {
              this._enabled ||
                (BM.Handler.prototype.enable.call(this),
                this.fire('enabled', {
                  handler: this.type,
                }),
                this._map.fire(BM.Draw.Event.DRAWSTART, {
                  layerType: this.type,
                }));
            },
            disable: function () {
              this._enabled &&
                (BM.Handler.prototype.disable.call(this),
                this._map.fire(BM.Draw.Event.DRAWSTOP, {
                  layerType: this.type,
                }),
                this.fire('disabled', {
                  handler: this.type,
                }));
            },
            addHooks: function () {
              var t = this._map;
              t &&
                (BM.DomUtil.disableTextSelection(),
                t.getContainer().focus(),
                (this._tooltip = new BM.Draw.Tooltip(this._map)),
                BM.DomEvent.on(this._container, 'keyup', this._cancelDrawing, this));
            },
            removeHooks: function () {
              this._map &&
                (BM.DomUtil.enableTextSelection(),
                this._tooltip.dispose(),
                (this._tooltip = null),
                BM.DomEvent.off(this._container, 'keyup', this._cancelDrawing, this));
            },
            setOptions: function (t) {
              BM.setOptions(this, t);
            },
            _fireCreatedEvent: function (t) {
              this._map.fire(BM.Draw.Event.CREATED, {
                layer: t,
                layerType: this.type,
              });
            },
            _cancelDrawing: function (t) {
              27 === t.keyCode &&
                (this._map.fire('draw:canceled', {
                  layerType: this.type,
                }),
                this.disable());
            },
          })),
          (BM.Draw.Polyline = BM.Draw.Feature.extend({
            statics: {
              TYPE: 'polyline',
            },
            Poly: BM.Polyline,
            options: {
              allowIntersection: !0,
              repeatMode: !1,
              drawError: {
                color: '#b00b00',
                timeout: 2500,
              },
              icon: new BM.DivIcon({
                iconSize: new BM.Point(8, 8),
                className: 'bigemap-div-icon bigemap-editing-icon',
              }),
              touchIcon: new BM.DivIcon({
                iconSize: new BM.Point(20, 20),
                className: 'bigemap-div-icon bigemap-editing-icon bigemap-touch-icon',
              }),
              guidelineDistance: 20,
              maxGuideLineLength: 4e3,
              shapeOptions: {
                stroke: !0,
                color: '#3388ff',
                weight: 4,
                opacity: 0.5,
                fill: !1,
                clickable: !0,
              },
              metric: !0,
              feet: !0,
              nautic: !1,
              showLength: !0,
              zIndexOffset: 2e3,
              factor: 1,
              maxPoints: 0,
            },
            initialize: function (t, e) {
              BM.Browser.touch && (this.options.icon = this.options.touchIcon),
                (this.options.drawError.message = BM.drawLocal.draw.handlers.polyline.error),
                e &&
                  e.drawError &&
                  (e.drawError = BM.Util.extend({}, this.options.drawError, e.drawError)),
                (this.type = BM.Draw.Polyline.TYPE),
                BM.Draw.Feature.prototype.initialize.call(this, t, e);
            },
            addHooks: function () {
              BM.Draw.Feature.prototype.addHooks.call(this),
                this._map &&
                  ((this._markers = []),
                  (this._markerGroup = new BM.LayerGroup()),
                  this._map.addLayer(this._markerGroup),
                  (this._clickHandle = !0),
                  (this._poly = new BM.Polyline([], this.options.shapeOptions)),
                  this._tooltip.updateContent(this._getTooltipText()),
                  this._mouseMarker ||
                    (this._mouseMarker = BM.marker(this._map.getCenter(), {
                      icon: BM.divIcon({
                        className: 'bigemap-mouse-marker',
                        iconAnchor: [20, 20],
                        iconSize: [40, 40],
                      }),
                      opacity: 0,
                      zIndexOffset: this.options.zIndexOffset,
                    })),
                  this._map
                    .on('mouseup', this._upEvent, this)
                    .on('mousemove', this._onMouseMove, this)
                    .on('zoomlevelschange', this._onZoomEnd, this)
                    .on('dragstart', this._dragStart, this)
                    .on('zoomend', this._onZoomEnd, this),
                  this._map.getContainer()._bindTouch ||
                    ((this._map.getContainer()._bindTouch = !0),
                    this._map
                      .getContainer()
                      .addEventListener('touchend', this._upEvent.bind(this))));
            },
            _dragStart: function () {
              this._drag = !0;
            },
            _upEvent: function (t) {
              if (
                !BM.Draw._clickHandled &&
                ((BM.Draw._clickHandled = !0),
                setTimeout(function () {
                  BM.Draw._clickHandled = !1;
                }, 100),
                this._clickHandle)
              ) {
                if (this._drag) return (this._drag = !1);
                var e,
                  i = t.originalEvent || t.changedTouches[0],
                  o = i.clientX,
                  n = i.clientY;
                this._disableNewMarkers(),
                  this._startPoint.call(this, o, n),
                  t.latlng ||
                    ((e = this._map.mouseEventToLayerPoint(i)),
                    (t.latlng = this._map.layerPointToLatLng(e))),
                  this._endPoint.call(this, o, n, t),
                  this._tttt ||
                    (this._tttt = {
                      x: 0,
                      y: 0,
                    }),
                  5 < Math.abs(this._tttt.x - o) &&
                    5 < Math.abs(this._tttt.y - n) &&
                    this._updateTooltip(t.latlng),
                  (this._tttt = {
                    x: o,
                    y: n,
                  }),
                  (this._touchHandled = null),
                  (this._clickHandled = null);
              }
            },
            removeHooks: function () {
              BM.Draw.Feature.prototype.removeHooks.call(this),
                (this._clickHandle = !1),
                this._clearHideErrorTimeout(),
                this._cleanUpShape(),
                this._map.removeLayer(this._markerGroup),
                delete this._markerGroup,
                delete this._markers,
                this._map.removeLayer(this._poly),
                delete this._poly,
                this._mouseMarker
                  .off('mousedown', this._onMouseDown, this)
                  .off('mouseout', this._onMouseOut, this)
                  .off('mouseup', this._onMouseUp, this)
                  .off('mousemove', this._onMouseMove, this),
                this._map.removeLayer(this._mouseMarker),
                delete this._mouseMarker,
                this._clearGuides(),
                this._map
                  .off('mouseup', this._upEvent, this)
                  .off('mousemove', this._onMouseMove, this)
                  .off('zoomlevelschange', this._onZoomEnd, this)
                  .off('dragstart', this._dragStart, this)
                  .off('zoomend', this._onZoomEnd, this);
            },
            deleteLastVertex: function () {
              var t, e, i, o;
              this._markers.length <= 1 ||
                ((t = this._markers.pop()),
                (o = (i = (e = this._poly).getLatLngs()).splice(-1, 1)[0]),
                this._poly.setLatLngs(i),
                this._markerGroup.removeLayer(t),
                e.getLatLngs().length < 2 && this._map.removeLayer(e),
                this._vertexChanged(o, !1));
            },
            addVertex: function (t) {
              2 <= this._markers.length &&
              !this.options.allowIntersection &&
              this._poly.newLatLngIntersects(t)
                ? this._showErrorTooltip()
                : (this._errorShown && this._hideErrorTooltip(),
                  this._markers.push(this._createMarker(t)),
                  this._poly.addLatLng(t),
                  2 === this._poly.getLatLngs().length && this._map.addLayer(this._poly),
                  this._vertexChanged(t, !0));
            },
            completeShape: function () {
              this._markers.length <= 1 ||
                !this._shapeIsValid() ||
                (this._fireCreatedEvent(),
                this.disable(),
                this.options.repeatMode && this.enable());
            },
            _finishShape: function () {
              var t = this._poly._defaultShape
                  ? this._poly._defaultShape()
                  : this._poly.getLatLngs(),
                e = this._poly.newLatLngIntersects(t[t.length - 1]);
              (!this.options.allowIntersection && e) || !this._shapeIsValid()
                ? this._showErrorTooltip()
                : (this._fireCreatedEvent(),
                  this.disable(),
                  this.options.repeatMode && this.enable());
            },
            _shapeIsValid: function () {
              return !0;
            },
            _onZoomEnd: function () {
              null !== this._markers && this._updateGuide();
            },
            _onMouseMove: function (t) {
              var e = this._map.mouseEventToLayerPoint(t.originalEvent),
                i = this._map.layerPointToLatLng(e);
              (this._currentLatLng = i),
                this._updateTooltip(i),
                this._updateGuide(e),
                this._mouseMarker.setLatLng(i),
                BM.DomEvent.preventDefault(t.originalEvent);
            },
            _vertexChanged: function (t, e) {
              this._map.fire(BM.Draw.Event.DRAWVERTEX, {
                layers: this._markerGroup,
              }),
                this._updateFinishHandler(),
                this._updateRunningMeasure(t, e),
                this._clearGuides(),
                this._updateTooltip();
            },
            _onMouseDown: function (t) {
              var e, i, o;
              this._clickHandled ||
                this._touchHandled ||
                this._disableMarkers ||
                (this._onMouseMove(t),
                (this._clickHandled = !0),
                this._disableNewMarkers(),
                (i = (e = t.originalEvent).clientX),
                (o = e.clientY),
                this._startPoint.call(this, i, o));
            },
            _startPoint: function (t, e) {
              this._mouseDownOrigin = BM.point(t, e);
            },
            _onMouseUp: function (t) {
              var e = t.originalEvent,
                i = e.clientX,
                o = e.clientY;
              this._endPoint.call(this, i, o, t), (this._clickHandled = null);
            },
            _endPoint: function (t, e, i) {
              var o, n;
              this._mouseDownOrigin &&
                ((o = BM.point(t, e).distanceTo(this._mouseDownOrigin)),
                (n = this._calculateFinishDistance(i.latlng)),
                1 < this.options.maxPoints && this.options.maxPoints == this._markers.length + 1
                  ? (this.addVertex(i.latlng), this._finishShape())
                  : n < 10 && BM.Browser.touch
                  ? this._finishShape()
                  : Math.abs(o) < 9 * (window.devicePixelRatio || 1) && this.addVertex(i.latlng),
                this._enableNewMarkers()),
                (this._mouseDownOrigin = null);
            },
            _onTouch: function (t) {
              var e,
                i,
                o = t.originalEvent;
              !o.touches ||
                !o.touches[0] ||
                this._clickHandled ||
                this._touchHandled ||
                this._disableMarkers ||
                ((e = o.touches[0].clientX),
                (i = o.touches[0].clientY),
                this._disableNewMarkers(),
                (this._touchHandled = !0),
                this._startPoint.call(this, e, i),
                this._endPoint.call(this, e, i, t),
                (this._touchHandled = null)),
                (this._clickHandled = null);
            },
            _onMouseOut: function () {
              this._tooltip && this._tooltip._onMouseOut.call(this._tooltip);
            },
            _calculateFinishDistance: function (t) {
              var e;
              if (0 < this._markers.length) {
                if (this.type === BM.Draw.Polyline.TYPE)
                  e = this._markers[this._markers.length - 1];
                else {
                  if (this.type !== BM.Draw.Polygon.TYPE) return 1 / 0;
                  e = this._markers[this._markers.length - 1];
                }
                var i = this._map.latLngToContainerPoint(e.getLatLng()),
                  o = new BM.Marker(t, {
                    icon: this.options.icon,
                    zIndexOffset: 2 * this.options.zIndexOffset,
                  }),
                  n = this._map.latLngToContainerPoint(o.getLatLng()),
                  a = i.distanceTo(n);
              } else a = 1 / 0;
              return a;
            },
            _updateFinishHandler: function () {
              var t = this._markers.length;
              2 < t && this._markers[t - 2].off('click', this._finishShape, this);
            },
            _createMarker: function (t) {
              var e = new BM.Marker(t, {
                icon: this.options.icon,
                zIndexOffset: 2 * this.options.zIndexOffset,
              });
              return this._markerGroup.addLayer(e), e;
            },
            _updateGuide: function (t) {
              var e = this._markers ? this._markers.length : 0;
              0 < e &&
                ((t = t || this._map.latLngToLayerPoint(this._currentLatLng)),
                this._clearGuides(),
                this._drawGuide(this._map.latLngToLayerPoint(this._markers[e - 1].getLatLng()), t));
            },
            _updateTooltip: function (t) {
              var e = this._getTooltipText();
              t && this._tooltip && this._tooltip.updatePosition(t),
                this._errorShown || (this._tooltip && this._tooltip.updateContent(e));
            },
            _drawGuide: function (t, e) {
              var i,
                o,
                n,
                a = Math.floor(Math.sqrt(Math.pow(e.x - t.x, 2) + Math.pow(e.y - t.y, 2))),
                s = this.options.guidelineDistance,
                r = this.options.maxGuideLineLength,
                h = r < a ? a - r : s;
              for (
                this._guidesContainer ||
                (this._guidesContainer = BM.DomUtil.create(
                  'div',
                  'bigemap-draw-guides',
                  this._overlayPane,
                ));
                h < a;
                h += this.options.guidelineDistance
              )
                (i = h / a),
                  (o = {
                    x: Math.floor(t.x * (1 - i) + i * e.x),
                    y: Math.floor(t.y * (1 - i) + i * e.y),
                  }),
                  ((n = BM.DomUtil.create(
                    'div',
                    'bigemap-draw-guide-dash',
                    this._guidesContainer,
                  )).style.backgroundColor = this._errorShown
                    ? this.options.drawError.color
                    : this.options.shapeOptions.color),
                  BM.DomUtil.setPosition(n, o);
            },
            _updateGuideColor: function (t) {
              if (this._guidesContainer)
                for (var e = 0, i = this._guidesContainer.childNodes.length; e < i; e++)
                  this._guidesContainer.childNodes[e].style.backgroundColor = t;
            },
            _clearGuides: function () {
              if (this._guidesContainer)
                for (; this._guidesContainer.firstChild; )
                  this._guidesContainer.removeChild(this._guidesContainer.firstChild);
            },
            _getTooltipText: function () {
              var t,
                e = this.options.showLength,
                i =
                  0 === this._markers.length
                    ? {
                        text: BM.drawLocal.draw.handlers.polyline.tooltip.start,
                      }
                    : ((t = e ? this._getMeasurementString() : ''),
                      1 === this._markers.length
                        ? {
                            text: BM.drawLocal.draw.handlers.polyline.tooltip.cont,
                            subtext: t,
                          }
                        : {
                            text: BM.drawLocal.draw.handlers.polyline.tooltip.end,
                            subtext: t,
                          });
              return i;
            },
            _updateRunningMeasure: function (t, e) {
              var i,
                o,
                n = this._markers.length;
              1 === this._markers.length
                ? (this._measurementRunningTotal = 0)
                : ((i = n - (e ? 2 : 1)),
                  (o = BM.GeometryUtil.isVersion07x()
                    ? t.distanceTo(this._markers[i].getLatLng()) * (this.options.factor || 1)
                    : this._map.distance(t, this._markers[i].getLatLng()) *
                      (this.options.factor || 1)),
                  (this._measurementRunningTotal += o * (e ? 1 : -1)));
            },
            _getMeasurementString: function () {
              var t = this._currentLatLng,
                e = this._markers[this._markers.length - 1].getLatLng(),
                i = BM.GeometryUtil.isVersion07x()
                  ? e && t && t.distanceTo
                    ? this._measurementRunningTotal + t.distanceTo(e) * (this.options.factor || 1)
                    : this._measurementRunningTotal || 0
                  : e && t
                  ? this._measurementRunningTotal +
                    this._map.distance(t, e) * (this.options.factor || 1)
                  : this._measurementRunningTotal || 0;
              return BM.GeometryUtil.readableDistance(
                i,
                this.options.metric,
                this.options.feet,
                this.options.nautic,
                this.options.precision,
              );
            },
            _showErrorTooltip: function () {
              (this._errorShown = !0),
                this._tooltip.showAsError().updateContent({
                  text: this.options.drawError.message,
                }),
                this._updateGuideColor(this.options.drawError.color),
                this._poly.setStyle({
                  color: this.options.drawError.color,
                }),
                this._clearHideErrorTimeout(),
                (this._hideErrorTimeout = setTimeout(
                  BM.Util.bind(this._hideErrorTooltip, this),
                  this.options.drawError.timeout,
                ));
            },
            _hideErrorTooltip: function () {
              (this._errorShown = !1),
                this._clearHideErrorTimeout(),
                this._tooltip.removeError().updateContent(this._getTooltipText()),
                this._updateGuideColor(this.options.shapeOptions.color),
                this._poly.setStyle({
                  color: this.options.shapeOptions.color,
                });
            },
            _clearHideErrorTimeout: function () {
              this._hideErrorTimeout &&
                (clearTimeout(this._hideErrorTimeout), (this._hideErrorTimeout = null));
            },
            _disableNewMarkers: function () {
              this._disableMarkers = !0;
            },
            _enableNewMarkers: function () {
              setTimeout(
                function () {
                  this._disableMarkers = !1;
                }.bind(this),
                50,
              );
            },
            _cleanUpShape: function () {
              1 < this._markers.length &&
                this._markers[this._markers.length - 1].off('click', this._finishShape, this);
            },
            _fireCreatedEvent: function () {
              var t = new this.Poly(this._poly.getLatLngs(), this.options.shapeOptions);
              BM.Draw.Feature.prototype._fireCreatedEvent.call(this, t);
            },
          })),
          (BM.Draw.Polygon = BM.Draw.Polyline.extend({
            statics: {
              TYPE: 'polygon',
            },
            Poly: BM.Polygon,
            options: {
              showArea: !1,
              showLength: !1,
              shapeOptions: {
                stroke: !0,
                color: '#3388ff',
                weight: 4,
                opacity: 0.5,
                fill: !0,
                fillColor: null,
                fillOpacity: 0.2,
                clickable: !0,
              },
              metric: !0,
              feet: !0,
              nautic: !1,
              precision: {},
            },
            initialize: function (t, e) {
              BM.Draw.Polyline.prototype.initialize.call(this, t, e),
                (this.type = BM.Draw.Polygon.TYPE);
            },
            _updateFinishHandler: function () {
              var t = this._markers.length;
              2 < t && 3 < t && this._markers[t - 2].off('dblclick', this._finishShape, this);
            },
            _getTooltipText: function () {
              var t, e;
              if (this._markers)
                return (
                  0 === this._markers.length
                    ? (t = BM.drawLocal.draw.handlers.polygon.tooltip.start)
                    : (e =
                        ((t =
                          this._markers.length < 3
                            ? BM.drawLocal.draw.handlers.polygon.tooltip.cont
                            : BM.drawLocal.draw.handlers.polygon.tooltip.end),
                        this._getMeasurementString())),
                  {
                    text: t,
                    subtext: e,
                  }
                );
            },
            _getMeasurementString: function () {
              var t = this._area,
                e = '';
              return t || this.options.showLength
                ? (this.options.showLength &&
                    (e = BM.Draw.Polyline.prototype._getMeasurementString.call(this)),
                  t &&
                    (e +=
                      '<br>' +
                      BM.GeometryUtil.readableArea(t, this.options.metric, this.options.precision)),
                  e)
                : null;
            },
            _shapeIsValid: function () {
              return 3 <= this._markers.length;
            },
            _vertexChanged: function (t, e) {
              var i;
              !this.options.allowIntersection &&
                this.options.showArea &&
                ((i = this._poly.getLatLngs()), (this._area = BM.GeometryUtil.geodesicArea(i))),
                BM.Draw.Polyline.prototype._vertexChanged.call(this, t, e);
            },
            _cleanUpShape: function () {
              var t = this._markers.length;
              0 < t &&
                (this._markers[0].off('click', this._finishShape, this),
                2 < t && this._markers[t - 1].off('dblclick', this._finishShape, this));
            },
          })),
          (BM.SimpleShape = {}),
          (BM.Draw.SimpleShape = BM.Draw.Feature.extend({
            options: {
              repeatMode: !1,
            },
            initialize: function (t, e) {
              (this._endLabelText = BM.drawLocal.draw.handlers.simpleshape.tooltip.end),
                BM.Draw.Feature.prototype.initialize.call(this, t, e);
            },
            addHooks: function () {
              BM.Draw.Feature.prototype.addHooks.call(this),
                this._map &&
                  ((this._mapDraggable = this._map.dragging.enabled()),
                  this._mapDraggable && this._map.dragging.disable(),
                  (this._container.style.cursor = 'crosshair'),
                  this._tooltip.updateContent({
                    text: this._initialLabelText,
                  }),
                  this._map
                    .on('mousedown', this._onMouseDown, this)
                    .on('mousemove', this._onMouseMove, this)
                    .on('touchstart', this._onMouseDown, this)
                    .on('touchmove', this._onMouseMove, this),
                  document.addEventListener('touchstart', BM.DomEvent.preventDefault, {
                    passive: !1,
                  }));
            },
            removeHooks: function () {
              BM.Draw.Feature.prototype.removeHooks.call(this),
                this._map &&
                  (this._mapDraggable && this._map.dragging.enable(),
                  (this._container.style.cursor = ''),
                  this._map
                    .off('mousedown', this._onMouseDown, this)
                    .off('mousemove', this._onMouseMove, this)
                    .off('touchstart', this._onMouseDown, this)
                    .off('touchmove', this._onMouseMove, this),
                  BM.DomEvent.off(document, 'mouseup', this._onMouseUp, this),
                  BM.DomEvent.off(document, 'touchend', this._onMouseUp, this),
                  document.removeEventListener('touchstart', BM.DomEvent.preventDefault),
                  this._shape && (this._map.removeLayer(this._shape), delete this._shape)),
                (this._isDrawing = !1);
            },
            _getTooltipText: function () {
              return {
                text: this._endLabelText,
              };
            },
            _onMouseDown: function (t) {
              (this._isDrawing = !0),
                (this._startLatLng = t.latlng),
                BM.DomEvent.on(document, 'mouseup', this._onMouseUp, this)
                  .on(document, 'touchend', this._onMouseUp, this)
                  .preventDefault(t.originalEvent);
            },
            _onMouseMove: function (t) {
              var e = t.latlng;
              this._tooltip.updatePosition(e),
                this._isDrawing &&
                  (this._tooltip.updateContent(this._getTooltipText()), this._drawShape(e));
            },
            _onMouseUp: function () {
              this._shape && this._fireCreatedEvent(),
                this.disable(),
                this.options.repeatMode && this.enable();
            },
          })),
          (BM.Draw.Rectangle = BM.Draw.SimpleShape.extend({
            statics: {
              TYPE: 'rectangle',
            },
            options: {
              shapeOptions: {
                stroke: !0,
                color: '#3388ff',
                weight: 4,
                opacity: 0.5,
                fill: !0,
                fillColor: null,
                fillOpacity: 0.2,
                clickable: !0,
              },
              showArea: !0,
              metric: !0,
            },
            initialize: function (t, e) {
              (this.type = BM.Draw.Rectangle.TYPE),
                (this._initialLabelText = BM.drawLocal.draw.handlers.rectangle.tooltip.start),
                BM.Draw.SimpleShape.prototype.initialize.call(this, t, e);
            },
            disable: function () {
              this._enabled &&
                ((this._isCurrentlyTwoClickDrawing = !1),
                BM.Draw.SimpleShape.prototype.disable.call(this));
            },
            _onMouseUp: function (t) {
              this._shape || this._isCurrentlyTwoClickDrawing
                ? (this._isCurrentlyTwoClickDrawing && !_hasAncestor(t.target, 'bigemap-pane')) ||
                  BM.Draw.SimpleShape.prototype._onMouseUp.call(this)
                : (this._isCurrentlyTwoClickDrawing = !0);
            },
            _drawShape: function (t) {
              this._shape
                ? this._shape.setBounds(new BM.LatLngBounds(this._startLatLng, t))
                : ((this._shape = new BM.Rectangle(
                    new BM.LatLngBounds(this._startLatLng, t),
                    this.options.shapeOptions,
                  )),
                  this._map.addLayer(this._shape));
            },
            _fireCreatedEvent: function () {
              var t = new BM.Rectangle(this._shape.getBounds(), this.options.shapeOptions);
              BM.Draw.SimpleShape.prototype._fireCreatedEvent.call(this, t);
            },
            _getTooltipText: function () {
              var t,
                e,
                i,
                o = BM.Draw.SimpleShape.prototype._getTooltipText.call(this),
                n = this._shape,
                a = this.options.showArea;
              return (
                n &&
                  ((t = this._shape._defaultShape
                    ? this._shape._defaultShape()
                    : this._shape.getLatLngs()),
                  (e = BM.GeometryUtil.geodesicArea(t)),
                  (i = a ? BM.GeometryUtil.readableArea(e, this.options.metric) : '')),
                {
                  text: o.text,
                  subtext: i,
                }
              );
            },
          })),
          (BM.Draw.Circle = BM.Draw.SimpleShape.extend({
            statics: {
              TYPE: 'circle',
            },
            options: {
              shapeOptions: {
                stroke: !0,
                color: '#3388ff',
                weight: 4,
                opacity: 0.5,
                fill: !0,
                fillColor: null,
                fillOpacity: 0.2,
                clickable: !0,
              },
              showRadius: !0,
              metric: !0,
              feet: !0,
              nautic: !1,
            },
            initialize: function (t, e) {
              (this.type = BM.Draw.Circle.TYPE),
                (this._initialLabelText = BM.drawLocal.draw.handlers.circle.tooltip.start),
                BM.Draw.SimpleShape.prototype.initialize.call(this, t, e);
            },
            _drawShape: function (t) {
              var e;
              (e = BM.GeometryUtil.isVersion07x()
                ? this._startLatLng.distanceTo(t)
                : this._map.distance(this._startLatLng, t)),
                this._shape
                  ? this._shape.setRadius(e)
                  : ((this._shape = new BM.Circle(this._startLatLng, e, this.options.shapeOptions)),
                    this._map.addLayer(this._shape));
            },
            _fireCreatedEvent: function () {
              var t = new BM.Circle(
                this._startLatLng,
                this._shape.getRadius(),
                this.options.shapeOptions,
              );
              BM.Draw.SimpleShape.prototype._fireCreatedEvent.call(this, t);
            },
            _onMouseMove: function (t) {
              var e,
                i,
                o = t.latlng,
                n = this.options.showRadius,
                a = this.options.metric;
              this._tooltip.updatePosition(o),
                this._isDrawing &&
                  (this._drawShape(o),
                  (e = this._shape.getRadius().toFixed(1)),
                  (i = ''),
                  n &&
                    (i =
                      BM.drawLocal.draw.handlers.circle.radius +
                      ': ' +
                      BM.GeometryUtil.readableDistance(
                        e,
                        a,
                        this.options.feet,
                        this.options.nautic,
                      )),
                  this._tooltip.updateContent({
                    text: this._endLabelText,
                    subtext: i,
                  }));
            },
          })),
          (BM.Draw.Marker = BM.Draw.Feature.extend({
            statics: {
              TYPE: 'marker',
            },
            options: {
              icon: new BM.Icon.Default(),
              repeatMode: !1,
              zIndexOffset: 2e3,
            },
            initialize: function (t, e) {
              (this.type = BM.Draw.Marker.TYPE),
                (this._initialLabelText = BM.drawLocal.draw.handlers.marker.tooltip.start),
                BM.Draw.Feature.prototype.initialize.call(this, t, e);
            },
            addHooks: function () {
              BM.Draw.Feature.prototype.addHooks.call(this),
                this._map &&
                  (this._tooltip.updateContent({
                    text: this._initialLabelText,
                  }),
                  this._mouseMarker ||
                    (this._mouseMarker = BM.marker(this._map.getCenter(), {
                      icon: BM.divIcon({
                        className: 'bigemap-mouse-marker',
                        iconAnchor: [20, 20],
                        iconSize: [40, 40],
                      }),
                      opacity: 0,
                      zIndexOffset: this.options.zIndexOffset,
                    })),
                  this._mouseMarker.on('click', this._onClick, this).addTo(this._map),
                  this._map.on('mousemove', this._onMouseMove, this),
                  this._map.on('click', this._onTouch, this));
            },
            removeHooks: function () {
              BM.Draw.Feature.prototype.removeHooks.call(this),
                this._map &&
                  (this._map.off('click', this._onClick, this).off('click', this._onTouch, this),
                  this._marker &&
                    (this._marker.off('click', this._onClick, this),
                    this._map.removeLayer(this._marker),
                    delete this._marker),
                  this._mouseMarker.off('click', this._onClick, this),
                  this._map.removeLayer(this._mouseMarker),
                  delete this._mouseMarker,
                  this._map.off('mousemove', this._onMouseMove, this));
            },
            _onMouseMove: function (t) {
              var e = t.latlng;
              this._tooltip.updatePosition(e),
                this._mouseMarker.setLatLng(e),
                this._marker
                  ? ((e = this._mouseMarker.getLatLng()), this._marker.setLatLng(e))
                  : ((this._marker = this._createMarker(e)),
                    this._marker.on('click', this._onClick, this),
                    this._map.on('click', this._onClick, this).addLayer(this._marker));
            },
            _createMarker: function (t) {
              return new BM.Marker(t, {
                icon: this.options.icon,
                zIndexOffset: this.options.zIndexOffset,
              });
            },
            _onClick: function () {
              this._fireCreatedEvent(), this.disable(), this.options.repeatMode && this.enable();
            },
            _onTouch: function (t) {
              this._onMouseMove(t), this._onClick();
            },
            _fireCreatedEvent: function () {
              var t = new BM.Marker.Touch(this._marker.getLatLng(), {
                icon: this.options.icon,
              });
              BM.Draw.Feature.prototype._fireCreatedEvent.call(this, t);
            },
          })),
          (BM.Draw.CircleMarker = BM.Draw.Marker.extend({
            statics: {
              TYPE: 'circlemarker',
            },
            options: {
              stroke: !0,
              color: '#3388ff',
              weight: 4,
              opacity: 0.5,
              fill: !0,
              fillColor: null,
              fillOpacity: 0.2,
              clickable: !0,
              zIndexOffset: 2e3,
            },
            initialize: function (t, e) {
              (this.type = BM.Draw.CircleMarker.TYPE),
                (this._initialLabelText = BM.drawLocal.draw.handlers.circlemarker.tooltip.start),
                BM.Draw.Feature.prototype.initialize.call(this, t, e);
            },
            _fireCreatedEvent: function () {
              var t = new BM.CircleMarker(this._marker.getLatLng(), this.options);
              BM.Draw.Feature.prototype._fireCreatedEvent.call(this, t);
            },
            _createMarker: function (t) {
              return new BM.CircleMarker(t, this.options);
            },
          })),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.Poly = BM.Handler.extend({
            initialize: function (t) {
              (this.latlngs = [t._latlngs]),
                t._holes && (this.latlngs = this.latlngs.concat(t._holes)),
                (this._poly = t),
                this._poly.on('revert-edited', this._updateLatLngs, this);
            },
            _defaultShape: function () {
              return !BM.Polyline._flat || BM.Polyline._flat(this._poly._latlngs)
                ? this._poly._latlngs
                : this._poly._latlngs[0];
            },
            _eachVertexHandler: function (t) {
              for (var e = 0; e < this._verticesHandlers.length; e++) t(this._verticesHandlers[e]);
            },
            addHooks: function () {
              this._initHandlers(),
                this._eachVertexHandler(function (t) {
                  t.addHooks();
                });
            },
            removeHooks: function () {
              this._eachVertexHandler(function (t) {
                t.removeHooks();
              });
            },
            updateMarkers: function () {
              this._eachVertexHandler(function (t) {
                t.updateMarkers();
              });
            },
            _initHandlers: function () {
              this._verticesHandlers = [];
              for (var t = 0; t < this.latlngs.length; t++)
                this._verticesHandlers.push(
                  new BM.Edit.PolyVerticesEdit(
                    this._poly,
                    this.latlngs[t],
                    this._poly.options.poly,
                  ),
                );
            },
            _updateLatLngs: function (t) {
              (this.latlngs = [t.layer._latlngs]),
                t.layer._holes && (this.latlngs = this.latlngs.concat(t.layer._holes));
            },
          })),
          (BM.Edit.PolyVerticesEdit = BM.Handler.extend({
            options: {
              icon: new BM.DivIcon({
                iconSize: new BM.Point(8, 8),
                className: 'bigemap-div-icon leaflet-editing-icon',
              }),
              touchIcon: new BM.DivIcon({
                iconSize: new BM.Point(8, 8),
                className: 'bigemap-draw-drag-icon',
              }),
              drawError: {
                color: '#b00b00',
                timeout: 1e3,
              },
            },
            initialize: function (t, e, i) {
              BM.Browser.touch && (this.options.icon = this.options.touchIcon),
                (this._poly = t),
                i &&
                  i.drawError &&
                  (i.drawError = BM.Util.extend({}, this.options.drawError, i.drawError)),
                (this._latlngs = e),
                BM.setOptions(this, i);
            },
            _defaultShape: function () {
              return !BM.Polyline._flat || BM.Polyline._flat(this._latlngs)
                ? this._latlngs
                : this._latlngs[0];
            },
            addHooks: function () {
              var t = this._poly,
                e = t._path;
              t instanceof BM.Polygon ||
                ((t.options.fill = !1), t.options.editing && (t.options.editing.fill = !1)),
                e &&
                  t.options.editing &&
                  t.options.editing.className &&
                  (t.options.original.className &&
                    t.options.original.className.split(' ').forEach(function (t) {
                      BM.DomUtil.removeClass(e, t);
                    }),
                  t.options.editing.className.split(' ').forEach(function (t) {
                    BM.DomUtil.addClass(e, t);
                  })),
                t.setStyle(t.options.editing),
                this._poly._map &&
                  ((this._map = this._poly._map),
                  this._markerGroup || this._initMarkers(),
                  this._poly._map.addLayer(this._markerGroup));
            },
            removeHooks: function () {
              var t = this._poly,
                e = t._path;
              e &&
                t.options.editing &&
                t.options.editing.className &&
                (t.options.editing.className.split(' ').forEach(function (t) {
                  BM.DomUtil.removeClass(e, t);
                }),
                t.options.original.className &&
                  t.options.original.className.split(' ').forEach(function (t) {
                    BM.DomUtil.addClass(e, t);
                  })),
                t.setStyle(t.options.original),
                t._map &&
                  (t._map.removeLayer(this._markerGroup),
                  delete this._markerGroup,
                  delete this._markers);
            },
            updateMarkers: function () {
              this._markerGroup.clearLayers(), this._initMarkers();
            },
            _initMarkers: function () {
              this._markerGroup || (this._markerGroup = new BM.LayerGroup()), (this._markers = []);
              for (var t, e, i, o, n = this._defaultShape(), a = 0, s = n.length; a < s; a++)
                (e = this._createMarker(n[a], a)).on('click', this._onMarkerClick, this),
                  e.on('contextmenu', this._onContextMenu, this),
                  this._markers.push(e);
              for (a = 0, t = s - 1; a < s; t = a++)
                (0 !== a || (BM.Polygon && this._poly instanceof BM.Polygon)) &&
                  ((i = this._markers[t]),
                  (o = this._markers[a]),
                  this._createMiddleMarker(i, o),
                  this._updatePrevNext(i, o));
            },
            _createMarker: function (t, e) {
              var i = new BM.Marker.Touch(t, {
                draggable: !0,
                icon: this.options.icon,
              });
              return (
                (i._origLatLng = t),
                (i._index = e),
                i
                  .on('dragstart', this._onMarkerDragStart, this)
                  .on('drag', this._onMarkerDrag, this)
                  .on('dragend', this._fireEdit, this)
                  .on('touchmove', this._onTouchMove, this)
                  .on('touchend', this._fireEdit, this)
                  .on('MSPointerMove', this._onTouchMove, this)
                  .on('MSPointerUp', this._fireEdit, this),
                this._markerGroup.addLayer(i),
                i
              );
            },
            _onMarkerDragStart: function () {
              this._poly.fire('editstart');
            },
            _spliceLatLngs: function () {
              var t = this._defaultShape(),
                e = [].splice.apply(t, arguments);
              return this._poly._convertLatLngs(t, !0), this._poly.redraw(), e;
            },
            _removeMarker: function (t) {
              var e = t._index;
              this._markerGroup.removeLayer(t),
                this._markers.splice(e, 1),
                this._spliceLatLngs(e, 1),
                this._updateIndexes(e, -1),
                t
                  .off('dragstart', this._onMarkerDragStart, this)
                  .off('drag', this._onMarkerDrag, this)
                  .off('dragend', this._fireEdit, this)
                  .off('touchmove', this._onMarkerDrag, this)
                  .off('touchend', this._fireEdit, this)
                  .off('click', this._onMarkerClick, this)
                  .off('MSPointerMove', this._onTouchMove, this)
                  .off('MSPointerUp', this._fireEdit, this);
            },
            _fireEdit: function () {
              (this._poly.edited = !0),
                this._poly.fire('edit'),
                this._poly._map.fire(BM.Draw.Event.EDITVERTEX, {
                  layers: this._markerGroup,
                  poly: this._poly,
                });
            },
            _onMarkerDrag: function (t) {
              var e,
                i,
                o = t.target,
                n = this._poly,
                a = BM.LatLngUtil.cloneLatLng(o._origLatLng);
              BM.extend(o._origLatLng, o._latlng),
                n.options.poly &&
                  ((e = n._map._editTooltip),
                  !n.options.poly.allowIntersection &&
                    n.intersects() &&
                    (BM.extend(o._origLatLng, a),
                    o.setLatLng(a),
                    (i = n.options.color),
                    n.setStyle({
                      color: this.options.drawError.color,
                    }),
                    e &&
                      e.updateContent({
                        text: BM.drawLocal.draw.handlers.polyline.error,
                      }),
                    setTimeout(function () {
                      n.setStyle({
                        color: i,
                      }),
                        e &&
                          e.updateContent({
                            text: BM.drawLocal.edit.handlers.edit.tooltip.text,
                            subtext: BM.drawLocal.edit.handlers.edit.tooltip.subtext,
                          });
                    }, 1e3))),
                o._middleLeft && o._middleLeft.setLatLng(this._getMiddleLatLng(o._prev, o)),
                o._middleRight && o._middleRight.setLatLng(this._getMiddleLatLng(o, o._next)),
                (this._poly._bounds._southWest = BM.latLng(1 / 0, 1 / 0)),
                (this._poly._bounds._northEast = BM.latLng(-1 / 0, -1 / 0));
              var s = this._poly.getLatLngs();
              this._poly._convertLatLngs(s, !0), this._poly.redraw(), this._poly.fire('editdrag');
            },
            _onMarkerClick: function (t) {
              var e = BM.Polygon && this._poly instanceof BM.Polygon ? 4 : 3,
                i = t.target;
              this._defaultShape().length < e ||
                (this._removeMarker(i),
                this._updatePrevNext(i._prev, i._next),
                i._middleLeft && this._markerGroup.removeLayer(i._middleLeft),
                i._middleRight && this._markerGroup.removeLayer(i._middleRight),
                i._prev && i._next
                  ? this._createMiddleMarker(i._prev, i._next)
                  : i._prev
                  ? i._next || (i._prev._middleRight = null)
                  : (i._next._middleLeft = null),
                this._fireEdit());
            },
            _onContextMenu: function (t) {
              var e = t.target;
              this._poly;
              this._poly._map.fire(BM.Draw.Event.MARKERCONTEXT, {
                marker: e,
                layers: this._markerGroup,
                poly: this._poly,
              }),
                BM.DomEvent.stopPropagation;
            },
            _onTouchMove: function (t) {
              var e = this._map.mouseEventToLayerPoint(t.originalEvent.touches[0]),
                i = this._map.layerPointToLatLng(e),
                o = t.target;
              BM.extend(o._origLatLng, i),
                o._middleLeft && o._middleLeft.setLatLng(this._getMiddleLatLng(o._prev, o)),
                o._middleRight && o._middleRight.setLatLng(this._getMiddleLatLng(o, o._next)),
                this._poly.redraw(),
                this.updateMarkers();
            },
            _updateIndexes: function (e, i) {
              this._markerGroup.eachLayer(function (t) {
                t._index > e && (t._index += i);
              });
            },
            _createMiddleMarker: function (e, i) {
              var o,
                n,
                t,
                a = this._getMiddleLatLng(e, i),
                s = this._createMarker(a);
              s.setOpacity(0.6),
                (e._middleRight = i._middleLeft = s),
                (n = function () {
                  s.off('touchmove', n, this);
                  var t = i._index;
                  (s._index = t),
                    s.off('click', o, this).on('click', this._onMarkerClick, this),
                    (a.lat = s.getLatLng().lat),
                    (a.lng = s.getLatLng().lng),
                    this._spliceLatLngs(t, 0, a),
                    this._markers.splice(t, 0, s),
                    s.setOpacity(1),
                    this._updateIndexes(t, 1),
                    i._index++,
                    this._updatePrevNext(e, s),
                    this._updatePrevNext(s, i),
                    this._poly.fire('editstart');
                }),
                (t = function () {
                  s.off('dragstart', n, this),
                    s.off('dragend', t, this),
                    s.off('touchmove', n, this),
                    this._createMiddleMarker(e, s),
                    this._createMiddleMarker(s, i);
                }),
                (o = function () {
                  n.call(this), t.call(this), this._fireEdit();
                }),
                s
                  .on('click', o, this)
                  .on('dragstart', n, this)
                  .on('dragend', t, this)
                  .on('touchmove', n, this),
                this._markerGroup.addLayer(s);
            },
            _updatePrevNext: function (t, e) {
              t && (t._next = e), e && (e._prev = t);
            },
            _getMiddleLatLng: function (t, e) {
              var i = this._poly._map,
                o = i.project(t.getLatLng()),
                n = i.project(e.getLatLng());
              return i.unproject(o._add(n)._divideBy(2));
            },
          })),
          BM.Polyline.addInitHook(function () {
            this.editing ||
              (BM.Edit.Poly &&
                ((this.editing = new BM.Edit.Poly(this)),
                this.options.editable && this.editing.enable()),
              this.on('add', function () {
                this.editing && this.editing.enabled() && this.editing.addHooks();
              }),
              this.on('remove', function () {
                this.editing && this.editing.enabled() && this.editing.removeHooks();
              }));
          }),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.SimpleShape = BM.Handler.extend({
            options: {
              moveIcon: new BM.DivIcon({
                iconSize: new BM.Point(8, 8),
                className: 'bigemap-div-icon bigemap-editing-icon bigemap-edit-move',
              }),
              resizeIcon: new BM.DivIcon({
                iconSize: new BM.Point(8, 8),
                className: 'bigemap-div-icon bigemap-editing-icon bigemap-edit-resize',
              }),
              touchMoveIcon: new BM.DivIcon({
                iconSize: new BM.Point(15, 15),
                className:
                  'bigemap-div-icon bigemap-editing-icon bigemap-edit-move bigemap-touch-icon',
              }),
              touchResizeIcon: new BM.DivIcon({
                iconSize: new BM.Point(15, 15),
                className:
                  'bigemap-div-icon bigemap-editing-icon bigemap-edit-resize bigemap-touch-icon',
              }),
            },
            initialize: function (t, e) {
              BM.Browser.touch &&
                ((this.options.moveIcon = this.options.touchMoveIcon),
                (this.options.resizeIcon = this.options.touchResizeIcon)),
                (this._shape = t),
                BM.Util.setOptions(this, e);
            },
            addHooks: function () {
              var t = this._shape;
              this._shape._map &&
                ((this._map = this._shape._map),
                t.setStyle(t.options.editing),
                t._map &&
                  ((this._map = t._map),
                  this._markerGroup || this._initMarkers(),
                  this._map.addLayer(this._markerGroup)));
            },
            removeHooks: function () {
              var t = this._shape;
              if ((t.setStyle(t.options.original), t._map)) {
                this._unbindMarker(this._moveMarker);
                for (var e = 0, i = this._resizeMarkers.length; e < i; e++)
                  this._unbindMarker(this._resizeMarkers[e]);
                (this._resizeMarkers = null),
                  this._map.removeLayer(this._markerGroup),
                  delete this._markerGroup;
              }
              this._map = null;
            },
            updateMarkers: function () {
              this._markerGroup.clearLayers(), this._initMarkers();
            },
            _initMarkers: function () {
              this._markerGroup || (this._markerGroup = new BM.LayerGroup()),
                this._createMoveMarker(),
                this._createResizeMarker();
            },
            _createMoveMarker: function () {},
            _createResizeMarker: function () {},
            _createMarker: function (t, e) {
              var i = new BM.Marker.Touch(t, {
                draggable: !0,
                icon: e,
                zIndexOffset: 10,
              });
              return this._bindMarker(i), this._markerGroup.addLayer(i), i;
            },
            _bindMarker: function (t) {
              t.on('dragstart', this._onMarkerDragStart, this)
                .on('drag', this._onMarkerDrag, this)
                .on('dragend', this._onMarkerDragEnd, this)
                .on('touchstart', this._onTouchStart, this)
                .on('touchmove', this._onTouchMove, this)
                .on('MSPointerMove', this._onTouchMove, this)
                .on('touchend', this._onTouchEnd, this)
                .on('MSPointerUp', this._onTouchEnd, this);
            },
            _unbindMarker: function (t) {
              t.off('dragstart', this._onMarkerDragStart, this)
                .off('drag', this._onMarkerDrag, this)
                .off('dragend', this._onMarkerDragEnd, this)
                .off('touchstart', this._onTouchStart, this)
                .off('touchmove', this._onTouchMove, this)
                .off('MSPointerMove', this._onTouchMove, this)
                .off('touchend', this._onTouchEnd, this)
                .off('MSPointerUp', this._onTouchEnd, this);
            },
            _onMarkerDragStart: function (t) {
              t.target.setOpacity(0), this._shape.fire('editstart');
            },
            _fireEdit: function () {
              (this._shape.edited = !0), this._shape.fire('edit');
            },
            _onMarkerDrag: function (t) {
              var e = t.target,
                i = e.getLatLng();
              e === this._moveMarker ? this._move(i) : this._resize(i),
                this._shape.redraw(),
                this._shape.fire('editdrag');
            },
            _onMarkerDragEnd: function (t) {
              t.target.setOpacity(1), this._fireEdit();
            },
            _onTouchStart: function (t) {
              var e, i, o;
              BM.Edit.SimpleShape.prototype._onMarkerDragStart.call(this, t),
                'function' == typeof this._getCorners &&
                  ((e = this._getCorners()),
                  (o = (i = t.target)._cornerIndex),
                  i.setOpacity(0),
                  (this._oppositeCorner = e[(o + 2) % 4]),
                  this._toggleCornerMarkers(0, o)),
                this._shape.fire('editstart');
            },
            _onTouchMove: function (t) {
              var e = this._map.mouseEventToLayerPoint(t.originalEvent.touches[0]),
                i = this._map.layerPointToLatLng(e);
              return (
                t.target === this._moveMarker ? this._move(i) : this._resize(i),
                this._shape.redraw(),
                !1
              );
            },
            _onTouchEnd: function (t) {
              t.target.setOpacity(1), this.updateMarkers(), this._fireEdit();
            },
            _move: function () {},
            _resize: function () {},
          })),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.Rectangle = BM.Edit.SimpleShape.extend({
            _createMoveMarker: function () {
              var t = this._shape.getBounds().getCenter();
              this._moveMarker = this._createMarker(t, this.options.moveIcon);
            },
            _createResizeMarker: function () {
              var t = this._getCorners();
              this._resizeMarkers = [];
              for (var e = 0, i = t.length; e < i; e++)
                this._resizeMarkers.push(this._createMarker(t[e], this.options.resizeIcon)),
                  (this._resizeMarkers[e]._cornerIndex = e);
            },
            _onMarkerDragStart: function (t) {
              BM.Edit.SimpleShape.prototype._onMarkerDragStart.call(this, t);
              var e = this._getCorners(),
                i = t.target._cornerIndex;
              (this._oppositeCorner = e[(i + 2) % 4]), this._toggleCornerMarkers(0, i);
            },
            _onMarkerDragEnd: function (t) {
              var e,
                i = t.target;
              i === this._moveMarker && ((e = this._shape.getBounds().getCenter()), i.setLatLng(e)),
                this._toggleCornerMarkers(1),
                this._repositionCornerMarkers(),
                BM.Edit.SimpleShape.prototype._onMarkerDragEnd.call(this, t);
            },
            _move: function (t) {
              for (
                var e,
                  i = this._shape._defaultShape
                    ? this._shape._defaultShape()
                    : this._shape.getLatLngs(),
                  o = this._shape.getBounds().getCenter(),
                  n = [],
                  a = 0,
                  s = i.length;
                a < s;
                a++
              )
                (e = [i[a].lat - o.lat, i[a].lng - o.lng]), n.push([t.lat + e[0], t.lng + e[1]]);
              this._shape.setLatLngs(n),
                this._repositionCornerMarkers(),
                this._map.fire(BM.Draw.Event.EDITMOVE, {
                  layer: this._shape,
                });
            },
            _resize: function (t) {
              var e;
              this._shape.setBounds(BM.latLngBounds(t, this._oppositeCorner)),
                (e = this._shape.getBounds()),
                this._moveMarker.setLatLng(e.getCenter()),
                this._map.fire(BM.Draw.Event.EDITRESIZE, {
                  layer: this._shape,
                });
            },
            _getCorners: function () {
              var t = this._shape.getBounds();
              return [t.getNorthWest(), t.getNorthEast(), t.getSouthEast(), t.getSouthWest()];
            },
            _toggleCornerMarkers: function (t) {
              for (var e = 0, i = this._resizeMarkers.length; e < i; e++)
                this._resizeMarkers[e].setOpacity(t);
            },
            _repositionCornerMarkers: function () {
              for (var t = this._getCorners(), e = 0, i = this._resizeMarkers.length; e < i; e++)
                this._resizeMarkers[e].setLatLng(t[e]);
            },
          })),
          BM.Rectangle.addInitHook(function () {
            BM.Edit.Rectangle &&
              ((this.editing = new BM.Edit.Rectangle(this)),
              this.options.editable && this.editing.enable());
          }),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.Marker = BM.Handler.extend({
            initialize: function (t, e) {
              (this._marker = t), BM.setOptions(this, e);
            },
            addHooks: function () {
              var t = this._marker;
              t.dragging.enable(),
                t.on('dragend', this._onDragEnd, t),
                this._toggleMarkerHighlight();
            },
            removeHooks: function () {
              var t = this._marker;
              t.dragging.disable(),
                t.off('dragend', this._onDragEnd, t),
                this._toggleMarkerHighlight();
            },
            _onDragEnd: function (t) {
              var e = t.target;
              (e.edited = !0),
                this._map.fire(BM.Draw.Event.EDITMOVE, {
                  layer: e,
                });
            },
            _toggleMarkerHighlight: function () {
              var t = this._marker._icon;
              t &&
                ((t.style.display = 'none'),
                BM.DomUtil.hasClass(t, 'leaflet-edit-marker-selected')
                  ? (BM.DomUtil.removeClass(t, 'leaflet-edit-marker-selected'),
                    this._offsetMarker(t, -4))
                  : (BM.DomUtil.addClass(t, 'leaflet-edit-marker-selected'),
                    this._offsetMarker(t, 4)),
                (t.style.display = ''));
            },
            _offsetMarker: function (t, e) {
              var i = parseInt(t.style.marginTop, 10) - e,
                o = parseInt(t.style.marginLeft, 10) - e;
              (t.style.marginTop = i + 'px'), (t.style.marginLeft = o + 'px');
            },
          })),
          BM.Marker.addInitHook(function () {
            BM.Edit.Marker &&
              ((this.editing = new BM.Edit.Marker(this)),
              this.options.editable && this.editing.enable());
          }),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.CircleMarker = BM.Edit.SimpleShape.extend({
            _createMoveMarker: function () {
              var t = this._shape.getLatLng();
              this._moveMarker = this._createMarker(t, this.options.moveIcon);
            },
            _createResizeMarker: function () {
              this._resizeMarkers = [];
            },
            _move: function (t) {
              var e;
              this._resizeMarkers.length &&
                ((e = this._getResizeMarkerPoint(t)), this._resizeMarkers[0].setLatLng(e)),
                this._shape.setLatLng(t),
                this._map.fire(BM.Draw.Event.EDITMOVE, {
                  layer: this._shape,
                });
            },
          })),
          BM.CircleMarker.addInitHook(function () {
            BM.Edit.CircleMarker &&
              ((this.editing = new BM.Edit.CircleMarker(this)),
              this.options.editable && this.editing.enable()),
              this.on('add', function () {
                this.editing && this.editing.enabled() && this.editing.addHooks();
              }),
              this.on('remove', function () {
                this.editing && this.editing.enabled() && this.editing.removeHooks();
              });
          }),
          (BM.Edit = BM.Edit || {}),
          (BM.Edit.Circle = BM.Edit.CircleMarker.extend({
            _createResizeMarker: function () {
              var t = this._shape.getLatLng(),
                e = this._getResizeMarkerPoint(t);
              (this._resizeMarkers = []),
                this._resizeMarkers.push(this._createMarker(e, this.options.resizeIcon));
            },
            _getResizeMarkerPoint: function (t) {
              var e = this._shape._radius * Math.cos(Math.PI / 4),
                i = this._map.project(t);
              return this._map.unproject([i.x + e, i.y - e]);
            },
            _resize: function (t) {
              var e = this._moveMarker.getLatLng();
              (radius = BM.GeometryUtil.isVersion07x()
                ? e.distanceTo(t)
                : this._map.distance(e, t)),
                this._shape.setRadius(radius),
                this._map.editTooltip &&
                  this._map._editTooltip.updateContent({
                    text:
                      BM.drawLocal.edit.handlers.edit.tooltip.subtext +
                      '<br />' +
                      BM.drawLocal.edit.handlers.edit.tooltip.text,
                    subtext:
                      BM.drawLocal.draw.handlers.circle.radius +
                      ': ' +
                      BM.GeometryUtil.readableDistance(
                        radius,
                        !0,
                        this.options.feet,
                        this.options.nautic,
                      ),
                  }),
                this._shape.setRadius(radius),
                this._map.fire(BM.Draw.Event.EDITRESIZE, {
                  layer: this._shape,
                });
            },
          })),
          BM.Circle.addInitHook(function () {
            BM.Edit.Circle &&
              ((this.editing = new BM.Edit.Circle(this)),
              this.options.editable && this.editing.enable());
          }),
          BM.Map.mergeOptions({
            touchExtend: !0,
          }),
          (BM.Map.TouchExtend = BM.Handler.extend({
            initialize: function (t) {
              (this._map = t),
                (this._container = t._container),
                (this._pane = t._panes.overlayPane);
            },
            addHooks: function () {
              BM.DomEvent.on(this._container, 'touchstart', this._onTouchStart, this),
                BM.DomEvent.on(this._container, 'touchend', this._onTouchEnd, this),
                BM.DomEvent.on(this._container, 'touchmove', this._onTouchMove, this),
                this._detectIE()
                  ? (BM.DomEvent.on(this._container, 'MSPointerDown', this._onTouchStart, this),
                    BM.DomEvent.on(this._container, 'MSPointerUp', this._onTouchEnd, this),
                    BM.DomEvent.on(this._container, 'MSPointerMove', this._onTouchMove, this),
                    BM.DomEvent.on(this._container, 'MSPointerCancel', this._onTouchCancel, this))
                  : (BM.DomEvent.on(this._container, 'touchcancel', this._onTouchCancel, this),
                    BM.DomEvent.on(this._container, 'touchleave', this._onTouchLeave, this));
            },
            removeHooks: function () {
              BM.DomEvent.off(this._container, 'touchstart', this._onTouchStart, this),
                BM.DomEvent.off(this._container, 'touchend', this._onTouchEnd, this),
                BM.DomEvent.off(this._container, 'touchmove', this._onTouchMove, this),
                this._detectIE()
                  ? (BM.DomEvent.off(this._container, 'MSPointerDown', this._onTouchStart, this),
                    BM.DomEvent.off(this._container, 'MSPointerUp', this._onTouchEnd, this),
                    BM.DomEvent.off(this._container, 'MSPointerMove', this._onTouchMove, this),
                    BM.DomEvent.off(this._container, 'MSPointerCancel', this._onTouchCancel, this))
                  : (BM.DomEvent.off(this._container, 'touchcancel', this._onTouchCancel, this),
                    BM.DomEvent.off(this._container, 'touchleave', this._onTouchLeave, this));
            },
            _touchEvent: function (t, e) {
              var i = {};
              if (void 0 !== t.touches) {
                if (!t.touches.length) return;
                i = t.touches[0];
              } else {
                if ('touch' !== t.pointerType) return;
                if (((i = t), !this._filterClick(t))) return;
              }
              var o = this._map.mouseEventToContainerPoint(i),
                n = this._map.mouseEventToLayerPoint(i),
                a = this._map.layerPointToLatLng(n);
              this._map.fire(e, {
                latlng: a,
                layerPoint: n,
                containerPoint: o,
                pageX: i.pageX,
                pageY: i.pageY,
                originalEvent: t,
              });
            },
            _filterClick: function (t) {
              var e = t.timeStamp || t.originalEvent.timeStamp,
                i = BM.DomEvent._lastClick && e - BM.DomEvent._lastClick;
              return (i && 100 < i && i < 500) || (t.target._simulatedClick && !t._simulated)
                ? (BM.DomEvent.stop(t), !1)
                : ((BM.DomEvent._lastClick = e), !0);
            },
            _onTouchStart: function (t) {
              this._map._loaded && this._touchEvent(t, 'touchstart');
            },
            _onTouchEnd: function (t) {
              this._map._loaded && this._touchEvent(t, 'touchend');
            },
            _onTouchCancel: function (t) {
              var e;
              this._map._loaded &&
                ((e = 'touchcancel'),
                this._detectIE() && (e = 'pointercancel'),
                this._touchEvent(t, e));
            },
            _onTouchLeave: function (t) {
              this._map._loaded && this._touchEvent(t, 'touchleave');
            },
            _onTouchMove: function (t) {
              this._map._loaded && this._touchEvent(t, 'touchmove');
            },
            _detectIE: function () {
              var t = window.navigator.userAgent,
                e = t.indexOf('MSIE ');
              if (0 < e) return parseInt(t.substring(e + 5, t.indexOf('.', e)), 10);
              if (0 < t.indexOf('Trident/')) {
                var i = t.indexOf('rv:');
                return parseInt(t.substring(i + 3, t.indexOf('.', i)), 10);
              }
              var o = t.indexOf('Edge/');
              return 0 < o && parseInt(t.substring(o + 5, t.indexOf('.', o)), 10);
            },
          })),
          BM.Map.addInitHook('addHandler', 'touchExtend', BM.Map.TouchExtend),
          (BM.Marker.Touch = BM.Marker.extend({
            _initInteraction: function () {
              return this.addInteractiveTarget
                ? BM.Marker.prototype._initInteraction.apply(this)
                : this._initInteractionLegacy();
            },
            _initInteractionLegacy: function () {
              if (this.options.clickable) {
                var t = this._icon,
                  e = [
                    'dblclick',
                    'mousedown',
                    'mouseover',
                    'mouseout',
                    'contextmenu',
                    'touchstart',
                    'touchend',
                    'touchmove',
                  ];
                this._detectIE
                  ? e.concat(['MSPointerDown', 'MSPointerUp', 'MSPointerMove', 'MSPointerCancel'])
                  : e.concat(['touchcancel']),
                  BM.DomUtil.addClass(t, 'bigemap-clickable'),
                  BM.DomEvent.on(t, 'click', this._onMouseClick, this),
                  BM.DomEvent.on(t, 'keypress', this._onKeyPress, this);
                for (var i = 0; i < e.length; i++)
                  BM.DomEvent.on(t, e[i], this._fireMouseEvent, this);
                BM.Handler.MarkerDrag &&
                  ((this.dragging = new BM.Handler.MarkerDrag(this)),
                  this.options.draggable && this.dragging.enable());
              }
            },
            _detectIE: function () {
              var t = window.navigator.userAgent,
                e = t.indexOf('MSIE ');
              if (0 < e) return parseInt(t.substring(e + 5, t.indexOf('.', e)), 10);
              if (0 < t.indexOf('Trident/')) {
                var i = t.indexOf('rv:');
                return parseInt(t.substring(i + 3, t.indexOf('.', i)), 10);
              }
              var o = t.indexOf('Edge/');
              return 0 < o && parseInt(t.substring(o + 5, t.indexOf('.', o)), 10);
            },
          })),
          (BM.LatLngUtil = {
            cloneLatLngs: function (t) {
              for (var e = [], i = 0, o = t.length; i < o; i++)
                Array.isArray(t[i])
                  ? e.push(BM.LatLngUtil.cloneLatLngs(t[i]))
                  : e.push(this.cloneLatLng(t[i]));
              return e;
            },
            cloneLatLng: function (t) {
              return BM.latLng(t.lat, t.lng);
            },
          }),
          (function () {
            var r = {
              km: 2,
              ha: 2,
              m: 0,
              mi: 2,
              ac: 2,
              yd: 0,
              ft: 0,
              nm: 2,
            };
            BM.GeometryUtil = BM.extend(BM.GeometryUtil || {}, {
              geodesicArea: function (t) {
                var e,
                  i,
                  o = t.length,
                  n = 0,
                  a = Math.PI / 180;
                if (2 < o) {
                  for (var s = 0; s < o; s++)
                    (e = t[s]),
                      (n +=
                        ((i = t[(s + 1) % o]).lng - e.lng) *
                        a *
                        (2 + Math.sin(e.lat * a) + Math.sin(i.lat * a)));
                  n = (6378137 * n * 6378137) / 2;
                }
                return Math.abs(n);
              },
              formattedNumber: function (t, e) {
                var i,
                  o = parseFloat(t).toFixed(e),
                  n = BM.drawLocal.format && BM.drawLocal.format.numeric,
                  a = n && n.delimiters,
                  s = a && a.thousands,
                  r = a && a.decimal;
                return (
                  (s || r) &&
                    ((i = o.split('.')),
                    (o = s ? i[0].replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1' + s) : i[0]),
                    (r = r || '.'),
                    1 < i.length && (o = o + r + i[1])),
                  o
                );
              },
              readableArea: function (t, e, i) {
                var o,
                  i = BM.Util.extend({}, r, i),
                  n = e
                    ? ((o = ['ha', 'm']),
                      (type = typeof e),
                      'string' === type ? (o = [e]) : 'boolean' !== type && (o = e),
                      1e6 <= t && -1 !== o.indexOf('km')
                        ? BM.GeometryUtil.formattedNumber(1e-6 * t, i.km) + ' km²'
                        : 1e4 <= t && -1 !== o.indexOf('ha')
                        ? BM.GeometryUtil.formattedNumber(1e-4 * t, i.ha) + ' ha'
                        : BM.GeometryUtil.formattedNumber(t, i.m) + ' m²')
                    : 3097600 <= (t /= 0.836127)
                    ? BM.GeometryUtil.formattedNumber(t / 3097600, i.mi) + ' mi²'
                    : 4840 <= t
                    ? BM.GeometryUtil.formattedNumber(t / 4840, i.ac) + ' acres'
                    : BM.GeometryUtil.formattedNumber(t, i.yd) + ' yd²';
                return n;
              },
              readableDistance: function (t, e, i, o, n) {
                var a,
                  n = BM.Util.extend({}, r, n),
                  s = e
                    ? 'string' == typeof e
                      ? e
                      : 'metric'
                    : i
                    ? 'feet'
                    : o
                    ? 'nauticalMile'
                    : 'yards';
                switch (s) {
                  case 'metric':
                    a =
                      1e3 < t
                        ? BM.GeometryUtil.formattedNumber(t / 1e3, n.km) + ' km'
                        : BM.GeometryUtil.formattedNumber(t, n.m) + ' m';
                    break;
                  case 'feet':
                    (t *= 3.28083), (a = BM.GeometryUtil.formattedNumber(t, n.ft) + ' ft');
                    break;
                  case 'nauticalMile':
                    (t *= 0.53996), (a = BM.GeometryUtil.formattedNumber(t / 1e3, n.nm) + ' nm');
                    break;
                  case 'yards':
                  default:
                    a =
                      1760 < (t *= 1.09361)
                        ? BM.GeometryUtil.formattedNumber(t / 1760, n.mi) + ' miles'
                        : BM.GeometryUtil.formattedNumber(t, n.yd) + ' yd';
                }
                return a;
              },
              isVersion07x: function () {
                var t = BM.version.split('.');
                return 0 === parseInt(t[0], 10) && 7 === parseInt(t[1], 10);
              },
            });
          })(),
          BM.Util.extend(BM.LineUtil, {
            segmentsIntersect: function (t, e, i, o) {
              return (
                this._checkCounterclockwise(t, i, o) !== this._checkCounterclockwise(e, i, o) &&
                this._checkCounterclockwise(t, e, i) !== this._checkCounterclockwise(t, e, o)
              );
            },
            _checkCounterclockwise: function (t, e, i) {
              return (i.y - t.y) * (e.x - t.x) > (e.y - t.y) * (i.x - t.x);
            },
          }),
          BM.Polyline.include({
            intersects: function () {
              var t,
                e,
                i,
                o = this._getProjectedPoints(),
                n = o ? o.length : 0;
              if (this._tooFewPointsForIntersection()) return !1;
              for (t = n - 1; 3 <= t; t--)
                if (((e = o[t - 1]), (i = o[t]), this._lineSegmentsIntersectsRange(e, i, t - 2)))
                  return !0;
              return !1;
            },
            newLatLngIntersects: function (t, e) {
              return !!this._map && this.newPointIntersects(this._map.latLngToLayerPoint(t), e);
            },
            newPointIntersects: function (t, e) {
              var i = this._getProjectedPoints(),
                o = i ? i.length : 0,
                n = i ? i[o - 1] : null,
                a = o - 2;
              return (
                !this._tooFewPointsForIntersection(1) &&
                this._lineSegmentsIntersectsRange(n, t, a, e ? 1 : 0)
              );
            },
            _tooFewPointsForIntersection: function (t) {
              var e = this._getProjectedPoints(),
                i = e ? e.length : 0;
              return (i += t || 0), !e || i <= 3;
            },
            _lineSegmentsIntersectsRange: function (t, e, i, o) {
              var n,
                a,
                s = this._getProjectedPoints();
              o = o || 0;
              for (var r = i; o < r; r--)
                if (((n = s[r - 1]), (a = s[r]), BM.LineUtil.segmentsIntersect(t, e, n, a)))
                  return !0;
              return !1;
            },
            _getProjectedPoints: function () {
              if (!this._defaultShape) return this._originalPoints;
              for (var t = [], e = this._defaultShape(), i = 0; i < e.length; i++)
                t.push(this._map.latLngToLayerPoint(e[i]));
              return t;
            },
          }),
          BM.Polygon.include({
            intersects: function () {
              var t,
                e,
                i,
                o,
                n = this._getProjectedPoints();
              return (
                !this._tooFewPointsForIntersection() &&
                (!!BM.Polyline.prototype.intersects.call(this) ||
                  ((t = n.length),
                  (e = n[0]),
                  (i = n[t - 1]),
                  (o = t - 2),
                  this._lineSegmentsIntersectsRange(i, e, o, 1)))
              );
            },
          }),
          (BM.Control.Draw = BM.Control.extend({
            options: {
              position: 'topleft',
              draw: {},
              edit: !1,
            },
            initialize: function (t) {
              if (BM.version < '0.7')
                throw new Error(
                  'Leaflet.draw 0.2.3+ requires Leaflet 0.7.0+. Download latest from https://github.com/Leaflet/Leaflet/',
                );
              var e;
              BM.Control.prototype.initialize.call(this, t),
                (this._toolbars = {}),
                BM.DrawToolbar &&
                  this.options.draw &&
                  ((e = new BM.DrawToolbar(this.options.draw)),
                  (this._toolbars[BM.DrawToolbar.TYPE] = e),
                  this._toolbars[BM.DrawToolbar.TYPE].on('enable', this._toolbarEnabled, this)),
                BM.EditToolbar &&
                  this.options.edit &&
                  ((e = new BM.EditToolbar(this.options.edit)),
                  (this._toolbars[BM.EditToolbar.TYPE] = e),
                  this._toolbars[BM.EditToolbar.TYPE].on('enable', this._toolbarEnabled, this)),
                (BM.toolbar = this);
            },
            onAdd: function (t) {
              var e,
                i,
                o = BM.DomUtil.create('div', 'bigemap-draw'),
                n = !1,
                a = 'bigemap-draw-toolbar-top';
              for (i in this._toolbars)
                this._toolbars.hasOwnProperty(i) &&
                  (e = this._toolbars[i].addToolbar(t)) &&
                  (n ||
                    (BM.DomUtil.hasClass(e, a) || BM.DomUtil.addClass(e.childNodes[0], a),
                    (n = !0)),
                  o.appendChild(e));
              return o;
            },
            onRemove: function () {
              for (var t in this._toolbars)
                this._toolbars.hasOwnProperty(t) && this._toolbars[t].removeToolbar();
            },
            setDrawingOptions: function (t) {
              for (var e in this._toolbars)
                this._toolbars[e] instanceof BM.DrawToolbar && this._toolbars[e].setOptions(t);
            },
            _toolbarEnabled: function (t) {
              var e,
                i = t.target;
              for (e in this._toolbars) this._toolbars[e] !== i && this._toolbars[e].disable();
            },
          })),
          BM.Map.mergeOptions({
            drawControlTooltips: !0,
            drawControl: !1,
          }),
          BM.Map.addInitHook(function () {
            this.options.drawControl &&
              ((this.drawControl = new BM.Control.Draw()), this.addControl(this.drawControl));
          }),
          (BM.Draw = BM.Draw || {}),
          (BM.Draw.Tooltip = BM.Class.extend({
            initialize: function (t) {
              (this._map = t),
                (this._popupPane = t._panes.popupPane),
                (this._visible = !1),
                (this._container = t.options.drawControlTooltips
                  ? BM.DomUtil.create('div', 'bigemap-draw-tooltip', this._popupPane)
                  : null),
                (this._singleLineLabel = !1),
                this._map.on('mouseout', this._onMouseOut, this);
            },
            dispose: function () {
              this._map.off('mouseout', this._onMouseOut, this),
                this._container &&
                  (this._popupPane.removeChild(this._container), (this._container = null));
            },
            updateContent: function (t) {
              return (
                this._container &&
                  ((t.subtext = t.subtext || ''),
                  0 !== t.subtext.length || this._singleLineLabel
                    ? 0 < t.subtext.length &&
                      this._singleLineLabel &&
                      (BM.DomUtil.removeClass(this._container, 'bigemap-draw-tooltip-single'),
                      (this._singleLineLabel = !1))
                    : (BM.DomUtil.addClass(this._container, 'bigemap-draw-tooltip-single'),
                      (this._singleLineLabel = !0)),
                  (this._container.innerHTML =
                    (0 < t.subtext.length
                      ? '<span class="bigemap-draw-tooltip-subtext">' + t.subtext + '</span><br />'
                      : '') +
                    '<span>' +
                    t.text +
                    '</span>'),
                  t.text || t.subtext
                    ? ((this._visible = !0), (this._container.style.visibility = 'inherit'))
                    : ((this._visible = !1), (this._container.style.visibility = 'hidden'))),
                this
              );
            },
            updatePosition: function (t) {
              var e = this._map.latLngToLayerPoint(t),
                i = this._container;
              return (
                this._container &&
                  (this._visible && (i.style.visibility = 'inherit'), BM.DomUtil.setPosition(i, e)),
                this
              );
            },
            showAsError: function () {
              return (
                this._container &&
                  BM.DomUtil.addClass(this._container, 'bigemap-error-draw-tooltip'),
                this
              );
            },
            removeError: function () {
              return (
                this._container &&
                  BM.DomUtil.removeClass(this._container, 'bigemap-error-draw-tooltip'),
                this
              );
            },
            _onMouseOut: function () {
              this._container && (this._container.style.visibility = 'hidden');
            },
          })),
          (BM.Toolbar = BM.Class.extend({
            initialize: function (t) {
              BM.setOptions(this, t),
                (this._modes = {}),
                (this._actionButtons = []),
                (this._activeMode = null);
              var e = BM.version.split('.');
              1 === parseInt(e[0], 10) && 2 <= parseInt(e[1], 10)
                ? BM.Toolbar.include(BM.Evented.prototype)
                : BM.Toolbar.include(BM.Mixin.Events);
            },
            enabled: function () {
              return null !== this._activeMode;
            },
            disable: function () {
              this.enabled() && this._activeMode.handler.disable();
            },
            addToolbar: function (t) {
              var e,
                i = BM.DomUtil.create('div', 'bigemap-draw-section'),
                o = 0,
                n = this._toolbarClass || '',
                a = this.getModeHandlers(t);
              for (
                this._toolbarContainer = BM.DomUtil.create(
                  'div',
                  'bigemap-draw-toolbar bigemap-bar',
                ),
                  this._map = t,
                  e = 0;
                e < a.length;
                e++
              )
                a[e].enabled &&
                  this._initModeHandler(a[e].handler, this._toolbarContainer, o++, n, a[e].title);
              if (o)
                return (
                  (this._lastButtonIndex = --o),
                  (this._actionsContainer = BM.DomUtil.create('ul', 'bigemap-draw-actions')),
                  i.appendChild(this._toolbarContainer),
                  i.appendChild(this._actionsContainer),
                  i
                );
            },
            removeToolbar: function () {
              for (var t in this._modes)
                this._modes.hasOwnProperty(t) &&
                  (this._disposeButton(
                    this._modes[t].button,
                    this._modes[t].handler.enable,
                    this._modes[t].handler,
                  ),
                  this._modes[t].handler.disable(),
                  this._modes[t].handler
                    .off('enabled', this._handlerActivated, this)
                    .off('disabled', this._handlerDeactivated, this));
              this._modes = {};
              for (var e = 0, i = this._actionButtons.length; e < i; e++)
                this._disposeButton(
                  this._actionButtons[e].button,
                  this._actionButtons[e].callback,
                  this,
                );
              (this._actionButtons = []), (this._actionsContainer = null);
            },
            _initModeHandler: function (t, e, i, o, n) {
              var a = t.type;
              (this._modes[a] = {}),
                (this._modes[a].handler = t),
                (this._modes[a].button = this._createButton({
                  type: a,
                  title: n,
                  className: o + '-' + a,
                  container: e,
                  callback: this._modes[a].handler.enable,
                  context: this._modes[a].handler,
                })),
                (this._modes[a].buttonIndex = i),
                this._modes[a].handler
                  .on('enabled', this._handlerActivated, this)
                  .on('disabled', this._handlerDeactivated, this);
            },
            _detectIOS: function () {
              return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
            },
            _createButton: function (t) {
              var e = BM.DomUtil.create('a', t.className || '', t.container),
                i = BM.DomUtil.create('span', 'sr-only', t.container);
              (e.href = '#'),
                e.appendChild(i),
                t.title && ((e.title = t.title), (i.innerHTML = t.title)),
                t.text && ((e.innerHTML = t.text), (i.innerHTML = t.text));
              var o = this._detectIOS() ? 'touchstart' : 'click';
              return (
                BM.DomEvent.on(e, 'click', BM.DomEvent.stopPropagation)
                  .on(e, 'mousedown', BM.DomEvent.stopPropagation)
                  .on(e, 'dblclick', BM.DomEvent.stopPropagation)
                  .on(e, 'touchstart', BM.DomEvent.stopPropagation)
                  .on(e, 'click', BM.DomEvent.preventDefault)
                  .on(e, o, t.callback, t.context),
                e
              );
            },
            _disposeButton: function (t, e) {
              var i = this._detectIOS() ? 'touchstart' : 'click';
              BM.DomEvent.off(t, 'click', BM.DomEvent.stopPropagation)
                .off(t, 'mousedown', BM.DomEvent.stopPropagation)
                .off(t, 'dblclick', BM.DomEvent.stopPropagation)
                .off(t, 'touchstart', BM.DomEvent.stopPropagation)
                .off(t, 'click', BM.DomEvent.preventDefault)
                .off(t, i, e);
            },
            _handlerActivated: function (t) {
              this.disable(),
                (this._activeMode = this._modes[t.handler]),
                BM.DomUtil.addClass(this._activeMode.button, 'bigemap-draw-toolbar-button-enabled'),
                this._showActionsToolbar(),
                this.fire('enable');
            },
            _handlerDeactivated: function () {
              this._hideActionsToolbar(),
                BM.DomUtil.removeClass(
                  this._activeMode.button,
                  'bigemap-draw-toolbar-button-enabled',
                ),
                (this._activeMode = null),
                this.fire('disable');
            },
            _createActions: function (t) {
              for (
                var e,
                  i,
                  o = this._actionsContainer,
                  n = this.getActions(t),
                  a = n.length,
                  s = 0,
                  r = this._actionButtons.length;
                s < r;
                s++
              )
                this._disposeButton(this._actionButtons[s].button, this._actionButtons[s].callback);
              for (this._actionButtons = []; o.firstChild; ) o.removeChild(o.firstChild);
              for (var h = 0; h < a; h++)
                ('enabled' in n[h] && !n[h].enabled) ||
                  ((e = BM.DomUtil.create('li', '', o)),
                  (i = this._createButton({
                    title: n[h].title,
                    text: n[h].text,
                    container: e,
                    callback: n[h].callback,
                    context: n[h].context,
                  })),
                  this._actionButtons.push({
                    button: i,
                    callback: n[h].callback,
                  }));
            },
            _showActionsToolbar: function () {
              var t = this._activeMode.buttonIndex,
                e = this._lastButtonIndex,
                i = this._activeMode.button.offsetTop - 1;
              this._createActions(this._activeMode.handler),
                (this._actionsContainer.style.top = i + 'px'),
                0 === t &&
                  (BM.DomUtil.addClass(this._toolbarContainer, 'bigemap-draw-toolbar-notop'),
                  BM.DomUtil.addClass(this._actionsContainer, 'bigemap-draw-actions-top')),
                t === e &&
                  (BM.DomUtil.addClass(this._toolbarContainer, 'bigemap-draw-toolbar-nobottom'),
                  BM.DomUtil.addClass(this._actionsContainer, 'bigemap-draw-actions-bottom')),
                (this._actionsContainer.style.display = 'block'),
                this._map.fire(BM.Draw.Event.TOOLBAROPENED);
            },
            _hideActionsToolbar: function () {
              (this._actionsContainer.style.display = 'none'),
                BM.DomUtil.removeClass(this._toolbarContainer, 'bigemap-draw-toolbar-notop'),
                BM.DomUtil.removeClass(this._toolbarContainer, 'bigemap-draw-toolbar-nobottom'),
                BM.DomUtil.removeClass(this._actionsContainer, 'bigemap-draw-actions-top'),
                BM.DomUtil.removeClass(this._actionsContainer, 'bigemap-draw-actions-bottom'),
                this._map.fire(BM.Draw.Event.TOOLBARCLOSED);
            },
          })),
          (BM.DrawToolbar = BM.Toolbar.extend({
            statics: {
              TYPE: 'draw',
            },
            options: {
              polyline: {},
              polygon: {},
              rectangle: {},
              circle: {},
              marker: {},
              circlemarker: {},
            },
            initialize: function (t) {
              for (var e in this.options)
                this.options.hasOwnProperty(e) &&
                  t[e] &&
                  (t[e] = BM.extend({}, this.options[e], t[e]));
              (this._toolbarClass = 'bigemap-draw-draw'),
                BM.Toolbar.prototype.initialize.call(this, t);
            },
            getModeHandlers: function (t) {
              return [
                {
                  enabled: this.options.polyline,
                  handler: new BM.Draw.Polyline(t, this.options.polyline),
                  title: BM.drawLocal.draw.toolbar.buttons.polyline,
                },
                {
                  enabled: this.options.polygon,
                  handler: new BM.Draw.Polygon(t, this.options.polygon),
                  title: BM.drawLocal.draw.toolbar.buttons.polygon,
                },
                {
                  enabled: this.options.rectangle,
                  handler: new BM.Draw.Rectangle(t, this.options.rectangle),
                  title: BM.drawLocal.draw.toolbar.buttons.rectangle,
                },
                {
                  enabled: this.options.circle,
                  handler: new BM.Draw.Circle(t, this.options.circle),
                  title: BM.drawLocal.draw.toolbar.buttons.circle,
                },
                {
                  enabled: this.options.marker,
                  handler: new BM.Draw.Marker(t, this.options.marker),
                  title: BM.drawLocal.draw.toolbar.buttons.marker,
                },
                {
                  enabled: this.options.circlemarker,
                  handler: new BM.Draw.CircleMarker(t, this.options.circlemarker),
                  title: BM.drawLocal.draw.toolbar.buttons.circlemarker,
                },
              ];
            },
            getActions: function (t) {
              return [
                {
                  enabled: t.completeShape,
                  title: BM.drawLocal.draw.toolbar.finish.title,
                  text: BM.drawLocal.draw.toolbar.finish.text,
                  callback: t.completeShape,
                  context: t,
                },
                {
                  enabled: t.deleteLastVertex,
                  title: BM.drawLocal.draw.toolbar.undo.title,
                  text: BM.drawLocal.draw.toolbar.undo.text,
                  callback: t.deleteLastVertex,
                  context: t,
                },
                {
                  title: BM.drawLocal.draw.toolbar.actions.title,
                  text: BM.drawLocal.draw.toolbar.actions.text,
                  callback: this.disable,
                  context: this,
                },
              ];
            },
            setOptions: function (t) {
              for (var e in (BM.setOptions(this, t), this._modes))
                this._modes.hasOwnProperty(e) &&
                  t.hasOwnProperty(e) &&
                  this._modes[e].handler.setOptions(t[e]);
            },
          })),
          (BM.EditToolbar = BM.Toolbar.extend({
            statics: {
              TYPE: 'edit',
            },
            options: {
              edit: {
                selectedPathOptions: {
                  dashArray: '10, 10',
                  fill: !0,
                  fillColor: '#fe57a1',
                  fillOpacity: 0.1,
                  maintainColor: !1,
                },
              },
              remove: {},
              poly: null,
              featureGroup: null,
            },
            initialize: function (t) {
              t.edit &&
                (void 0 === t.edit.selectedPathOptions &&
                  (t.edit.selectedPathOptions = this.options.edit.selectedPathOptions),
                (t.edit.selectedPathOptions = BM.extend(
                  {},
                  this.options.edit.selectedPathOptions,
                  t.edit.selectedPathOptions,
                ))),
                t.remove && (t.remove = BM.extend({}, this.options.remove, t.remove)),
                t.poly && (t.poly = BM.extend({}, this.options.poly, t.poly)),
                (this._toolbarClass = 'bigemap-draw-edit'),
                BM.Toolbar.prototype.initialize.call(this, t),
                (this._selectedFeatureCount = 0);
            },
            getModeHandlers: function (t) {
              var e = this.options.featureGroup;
              return [
                {
                  enabled: this.options.edit,
                  handler: new BM.EditToolbar.Edit(t, {
                    featureGroup: e,
                    selectedPathOptions: this.options.edit.selectedPathOptions,
                    poly: this.options.poly,
                  }),
                  title: BM.drawLocal.edit.toolbar.buttons.edit,
                },
                {
                  enabled: this.options.remove,
                  handler: new BM.EditToolbar.Delete(t, {
                    featureGroup: e,
                  }),
                  title: BM.drawLocal.edit.toolbar.buttons.remove,
                },
              ];
            },
            getActions: function (t) {
              var e = [
                {
                  title: BM.drawLocal.edit.toolbar.actions.save.title,
                  text: BM.drawLocal.edit.toolbar.actions.save.text,
                  callback: this._save,
                  context: this,
                },
                {
                  title: BM.drawLocal.edit.toolbar.actions.cancel.title,
                  text: BM.drawLocal.edit.toolbar.actions.cancel.text,
                  callback: this.disable,
                  context: this,
                },
              ];
              return (
                t.removeAllLayers &&
                  e.push({
                    title: BM.drawLocal.edit.toolbar.actions.clearAll.title,
                    text: BM.drawLocal.edit.toolbar.actions.clearAll.text,
                    callback: this._clearAllLayers,
                    context: this,
                  }),
                e
              );
            },
            addToolbar: function (t) {
              var e = BM.Toolbar.prototype.addToolbar.call(this, t);
              return (
                this._checkDisabled(),
                this.options.featureGroup.on('layeradd layerremove', this._checkDisabled, this),
                e
              );
            },
            removeToolbar: function () {
              this.options.featureGroup.off('layeradd layerremove', this._checkDisabled, this),
                BM.Toolbar.prototype.removeToolbar.call(this);
            },
            disable: function () {
              this.enabled() &&
                (this._activeMode.handler.revertLayers(), BM.Toolbar.prototype.disable.call(this));
            },
            _save: function () {
              this._activeMode.handler.save(),
                this._activeMode && this._activeMode.handler.disable();
            },
            _clearAllLayers: function () {
              this._activeMode.handler.removeAllLayers(),
                this._activeMode && this._activeMode.handler.disable();
            },
            _checkDisabled: function () {
              var t,
                e = 0 !== this.options.featureGroup.getLayers().length;
              this.options.edit &&
                ((t = this._modes[BM.EditToolbar.Edit.TYPE].button),
                e
                  ? BM.DomUtil.removeClass(t, 'bigemap-disabled')
                  : BM.DomUtil.addClass(t, 'bigemap-disabled'),
                t.setAttribute(
                  'title',
                  e
                    ? BM.drawLocal.edit.toolbar.buttons.edit
                    : BM.drawLocal.edit.toolbar.buttons.editDisabled,
                )),
                this.options.remove &&
                  ((t = this._modes[BM.EditToolbar.Delete.TYPE].button),
                  e
                    ? BM.DomUtil.removeClass(t, 'bigemap-disabled')
                    : BM.DomUtil.addClass(t, 'bigemap-disabled'),
                  t.setAttribute(
                    'title',
                    e
                      ? BM.drawLocal.edit.toolbar.buttons.remove
                      : BM.drawLocal.edit.toolbar.buttons.removeDisabled,
                  ));
            },
          })),
          (BM.EditToolbar.Edit = BM.Handler.extend({
            statics: {
              TYPE: 'edit',
            },
            initialize: function (t, e) {
              if (
                (BM.Handler.prototype.initialize.call(this, t),
                BM.setOptions(this, e),
                (this._featureGroup = e.featureGroup),
                !(this._featureGroup instanceof BM.FeatureGroup))
              )
                throw new Error('options.featureGroup must be a BM.FeatureGroup');
              (this._uneditedLayerProps = {}), (this.type = BM.EditToolbar.Edit.TYPE);
              var i = BM.version.split('.');
              1 === parseInt(i[0], 10) && 2 <= parseInt(i[1], 10)
                ? BM.EditToolbar.Edit.include(BM.Evented.prototype)
                : BM.EditToolbar.Edit.include(BM.Mixin.Events);
            },
            enable: function () {
              !this._enabled &&
                this._hasAvailableLayers() &&
                (this.fire('enabled', {
                  handler: this.type,
                }),
                this._map.fire(BM.Draw.Event.EDITSTART, {
                  handler: this.type,
                }),
                BM.Handler.prototype.enable.call(this),
                this._featureGroup
                  .on('layeradd', this._enableLayerEdit, this)
                  .on('layerremove', this._disableLayerEdit, this));
            },
            disable: function () {
              this._enabled &&
                (this._featureGroup
                  .off('layeradd', this._enableLayerEdit, this)
                  .off('layerremove', this._disableLayerEdit, this),
                BM.Handler.prototype.disable.call(this),
                this._map.fire(BM.Draw.Event.EDITSTOP, {
                  handler: this.type,
                }),
                this.fire('disabled', {
                  handler: this.type,
                }));
            },
            addHooks: function () {
              var t = this._map;
              t &&
                (t.getContainer().focus(),
                this._featureGroup.eachLayer(this._enableLayerEdit, this),
                (this._tooltip = new BM.Draw.Tooltip(this._map)),
                this._tooltip.updateContent({
                  text: BM.drawLocal.edit.handlers.edit.tooltip.text,
                  subtext: BM.drawLocal.edit.handlers.edit.tooltip.subtext,
                }),
                (t._editTooltip = this._tooltip),
                this._updateTooltip(),
                this._map
                  .on('mousemove', this._onMouseMove, this)
                  .on('touchmove', this._onMouseMove, this)
                  .on('MSPointerMove', this._onMouseMove, this)
                  .on(BM.Draw.Event.EDITVERTEX, this._updateTooltip, this));
            },
            removeHooks: function () {
              this._map &&
                (this._featureGroup.eachLayer(this._disableLayerEdit, this),
                (this._uneditedLayerProps = {}),
                this._tooltip.dispose(),
                (this._tooltip = null),
                this._map
                  .off('mousemove', this._onMouseMove, this)
                  .off('touchmove', this._onMouseMove, this)
                  .off('MSPointerMove', this._onMouseMove, this)
                  .off(BM.Draw.Event.EDITVERTEX, this._updateTooltip, this));
            },
            revertLayers: function () {
              this._featureGroup.eachLayer(function (t) {
                this._revertLayer(t);
              }, this);
            },
            save: function () {
              var e = new BM.LayerGroup();
              this._featureGroup.eachLayer(function (t) {
                t.edited && (e.addLayer(t), (t.edited = !1));
              }),
                this._map.fire(BM.Draw.Event.EDITED, {
                  layers: e,
                });
            },
            _backupLayer: function (t) {
              var e = BM.Util.stamp(t);
              this._uneditedLayerProps[e] ||
                (t instanceof BM.Polyline || t instanceof BM.Polygon || t instanceof BM.Rectangle
                  ? (this._uneditedLayerProps[e] = {
                      latlngs: BM.LatLngUtil.cloneLatLngs(t.getLatLngs()),
                    })
                  : t instanceof BM.Circle
                  ? (this._uneditedLayerProps[e] = {
                      latlng: BM.LatLngUtil.cloneLatLng(t.getLatLng()),
                      radius: t.getRadius(),
                    })
                  : (t instanceof BM.Marker || t instanceof BM.CircleMarker) &&
                    (this._uneditedLayerProps[e] = {
                      latlng: BM.LatLngUtil.cloneLatLng(t.getLatLng()),
                    }));
            },
            _getTooltipText: function () {
              return {
                text: BM.drawLocal.edit.handlers.edit.tooltip.text,
                subtext: BM.drawLocal.edit.handlers.edit.tooltip.subtext,
              };
            },
            _updateTooltip: function () {
              this._tooltip.updateContent(this._getTooltipText());
            },
            _revertLayer: function (t) {
              var e = BM.Util.stamp(t);
              (t.edited = !1),
                this._uneditedLayerProps.hasOwnProperty(e) &&
                  (t instanceof BM.Polyline || t instanceof BM.Polygon || t instanceof BM.Rectangle
                    ? t.setLatLngs(this._uneditedLayerProps[e].latlngs)
                    : t instanceof BM.Circle
                    ? (t.setLatLng(this._uneditedLayerProps[e].latlng),
                      t.setRadius(this._uneditedLayerProps[e].radius))
                    : (t instanceof BM.Marker || t instanceof BM.CircleMarker) &&
                      t.setLatLng(this._uneditedLayerProps[e].latlng),
                  t.fire('revert-edited', {
                    layer: t,
                  }));
            },
            _enableLayerEdit: function (t) {
              var e,
                i,
                o = t.layer || t.target || t;
              this._backupLayer(o),
                this.options.poly &&
                  ((i = BM.Util.extend({}, this.options.poly)), (o.options.poly = i)),
                this.options.selectedPathOptions &&
                  ((e = BM.Util.extend({}, this.options.selectedPathOptions)).maintainColor &&
                    ((e.color = o.options.color), (e.fillColor = o.options.fillColor)),
                  (o.options.original = BM.extend({}, o.options)),
                  (o.options.editing = e)),
                o instanceof BM.Marker
                  ? (o.editing && o.editing.enable(),
                    o.dragging.enable(),
                    o
                      .on('dragend', this._onMarkerDragEnd)
                      .on('touchmove', this._onTouchMove, this)
                      .on('MSPointerMove', this._onTouchMove, this)
                      .on('touchend', this._onMarkerDragEnd, this)
                      .on('MSPointerUp', this._onMarkerDragEnd, this))
                  : o.editing.enable();
            },
            _disableLayerEdit: function (t) {
              var e = t.layer || t.target || t;
              (e.edited = !1),
                e.editing && e.editing.disable(),
                delete e.options.editing,
                delete e.options.original,
                this._selectedPathOptions &&
                  (e instanceof BM.Marker
                    ? this._toggleMarkerHighlight(e)
                    : (e.setStyle(e.options.previousOptions), delete e.options.previousOptions)),
                e instanceof BM.Marker
                  ? (e.dragging.disable(),
                    e
                      .off('dragend', this._onMarkerDragEnd, this)
                      .off('touchmove', this._onTouchMove, this)
                      .off('MSPointerMove', this._onTouchMove, this)
                      .off('touchend', this._onMarkerDragEnd, this)
                      .off('MSPointerUp', this._onMarkerDragEnd, this))
                  : e.editing.disable();
            },
            _onMouseMove: function (t) {
              this._tooltip.updatePosition(t.latlng);
            },
            _onMarkerDragEnd: function (t) {
              var e = t.target;
              (e.edited = !0),
                this._map.fire(BM.Draw.Event.EDITMOVE, {
                  layer: e,
                });
            },
            _onTouchMove: function (t) {
              var e = t.originalEvent.changedTouches[0],
                i = this._map.mouseEventToLayerPoint(e),
                o = this._map.layerPointToLatLng(i);
              t.target.setLatLng(o);
            },
            _hasAvailableLayers: function () {
              return 0 !== this._featureGroup.getLayers().length;
            },
          })),
          (BM.EditToolbar.Delete = BM.Handler.extend({
            statics: {
              TYPE: 'remove',
            },
            initialize: function (t, e) {
              if (
                (BM.Handler.prototype.initialize.call(this, t),
                BM.Util.setOptions(this, e),
                (this._deletableLayers = this.options.featureGroup),
                !(this._deletableLayers instanceof BM.FeatureGroup))
              )
                throw new Error('options.featureGroup must be a BM.FeatureGroup');
              this.type = BM.EditToolbar.Delete.TYPE;
              var i = BM.version.split('.');
              1 === parseInt(i[0], 10) && 2 <= parseInt(i[1], 10)
                ? BM.EditToolbar.Delete.include(BM.Evented.prototype)
                : BM.EditToolbar.Delete.include(BM.Mixin.Events);
            },
            enable: function () {
              !this._enabled &&
                this._hasAvailableLayers() &&
                (this.fire('enabled', {
                  handler: this.type,
                }),
                this._map.fire(BM.Draw.Event.DELETESTART, {
                  handler: this.type,
                }),
                BM.Handler.prototype.enable.call(this),
                this._deletableLayers
                  .on('layeradd', this._enableLayerDelete, this)
                  .on('layerremove', this._disableLayerDelete, this));
            },
            disable: function () {
              this._enabled &&
                (this._deletableLayers
                  .off('layeradd', this._enableLayerDelete, this)
                  .off('layerremove', this._disableLayerDelete, this),
                BM.Handler.prototype.disable.call(this),
                this._map.fire(BM.Draw.Event.DELETESTOP, {
                  handler: this.type,
                }),
                this.fire('disabled', {
                  handler: this.type,
                }));
            },
            addHooks: function () {
              var t = this._map;
              t &&
                (t.getContainer().focus(),
                this._deletableLayers.eachLayer(this._enableLayerDelete, this),
                (this._deletedLayers = new BM.LayerGroup()),
                (this._tooltip = new BM.Draw.Tooltip(this._map)),
                this._tooltip.updateContent({
                  text: BM.drawLocal.edit.handlers.remove.tooltip.text,
                }),
                this._map.on('mousemove', this._onMouseMove, this));
            },
            removeHooks: function () {
              this._map &&
                (this._deletableLayers.eachLayer(this._disableLayerDelete, this),
                (this._deletedLayers = null),
                this._tooltip.dispose(),
                (this._tooltip = null),
                this._map.off('mousemove', this._onMouseMove, this));
            },
            revertLayers: function () {
              this._deletedLayers.eachLayer(function (t) {
                this._deletableLayers.addLayer(t),
                  t.fire('revert-deleted', {
                    layer: t,
                  });
              }, this);
            },
            save: function () {
              this._map.fire(BM.Draw.Event.DELETED, {
                layers: this._deletedLayers,
              });
            },
            removeAllLayers: function () {
              this._deletableLayers.eachLayer(function (t) {
                this._removeLayer({
                  layer: t,
                });
              }, this),
                this.save();
            },
            _enableLayerDelete: function (t) {
              (t.layer || t.target || t).on('click', this._removeLayer, this);
            },
            _disableLayerDelete: function (t) {
              var e = t.layer || t.target || t;
              e.off('click', this._removeLayer, this), this._deletedLayers.removeLayer(e);
            },
            _removeLayer: function (t) {
              var e = t.layer || t.target || t;
              this._deletableLayers.removeLayer(e),
                this._deletedLayers.addLayer(e),
                e.fire('deleted');
            },
            _onMouseMove: function (t) {
              this._tooltip.updatePosition(t.latlng);
            },
            _hasAvailableLayers: function () {
              return 0 !== this._deletableLayers.getLayers().length;
            },
          }));

        //#endregion

        // let marker = BM.marker(map.getCenter(), { draggable: true }).addTo(map);
        //创建一个图形覆盖物的集合来保存点线面
        let drawnItems = new BM.FeatureGroup();
        //添加在地图上
        map.addLayer(drawnItems);
        // 为多边形设置一个标题
        BM.drawLocal.draw.toolbar.buttons.polygon = '添加一个多边形';

        //实例化鼠标绘制的控件
        var drawControl = new BM.Control.Draw({
          position: 'bottomright', //位置
          //控制绘制的图形
          draw: {
            polyline: {
              //单独设置线的颜色为红色，其它为默认颜色
              shapeOptions: {
                color: 'red',
              },
            },
            polygon: true,
            circle: true,
            marker: true,
          },
          edit: { featureGroup: drawnItems },
        });
        map.addControl(drawControl);
        //监听绘画完成事件
        map.on(BM.Draw.Event.CREATED, function (e) {
          var type = e.layerType,
            layer = e.layer;
          if (type === 'polygon') {
            // console.log(layer.editing.latlngs[0][0]);
            let params = {
              name: '',
              path: JSON.stringify(layer.editing.latlngs[0][0]),
            };
            createOrUpdate(params, false).then(()=>{
              message.success(`创建成功`);
            });
            
            refresh()
          }
          if (type === 'marker') {
            let params = {
              name: '',
              path: JSON.stringify(layer.editing._marker._latlng),
            };
            PcreateOrUpdate(params, false).then(()=>{
              message.success(`创建成功`);
            });
            refresh()
          }
          drawnItems.addLayer(layer);
        });
      });
    });
    return {
      areaId,
      areaName,
      areaPath,
      pointId,
      pointName,
      pointPath,
      area,
      point,
      getPoint,
      getArea,
      deleteArea,
      deletePoint,
      modalText,
      visible,
      Pvisible,
      confirmLoading,
      showModal,
      handleOk,
      PshowModal,
      PhandleOk,
    };
  },
});
</script>
<style scoped>
.bigemap-draw-section {
  top: 50px;
}
.inp {
  width: 30vh;
}
.modal {
  
}
.name{
  margin: 3vh
}
.deleteBtn{
  float: right;
}
</style>
