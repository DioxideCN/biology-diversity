

import { defineStore } from 'pinia';
import { store } from '/@/store';

export interface FullScreenState {
  isFullScreen: boolean;
}

export const useAppStore = defineStore({
  id: 'fullScreen',
  state: (): FullScreenState => ({
    isFullScreen:false
  }),

  actions: {
    setFullScreen(isFullScreen: boolean): void {
      this.isFullScreen = isFullScreen;
    },
  },
});

// Need to be used outside the setup
export function useAppStoreWithOut() {
  return useAppStore(store);
}
