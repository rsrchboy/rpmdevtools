;; $Id: rpmdevtools-init.el,v 1.1 2006/07/17 20:02:12 scop Exp $

(defun rpmdevtools-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (if buffer-file-name
      (call-process "newrpmspec" nil t nil "-o" "-" buffer-file-name)
    (call-process "newrpmspec" nil t nil "-o" "-"))
  (and indent-tabs-mode (tabify (point-min) (point-max)))
  (goto-char (point-min))
  (re-search-forward "^[A-Za-z]+:\\s-*$" nil t)
  (set-buffer-modified-p nil))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'rpmdevtools-new-rpm-spec-file-init t)
